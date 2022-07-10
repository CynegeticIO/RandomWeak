# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:56:51 2022

@author: CynegeticIO
"""

class ECPoint:
    gmpy2 = None
    #import gmpy2
    import random
    
    class InvError(Exception):
        def __init__(self, *pargs):
            self.value = pargs
    
    @classmethod
    def Int(cls, x):
        return int(x) if cls.gmpy2 is None else cls.gmpy2.mpz(x)
    
    @classmethod
    def std_point(cls, t):
        if t == 'secp256k1':
            # https://en.bitcoin.it/wiki/Secp256k1
            # https://www.secg.org/sec2-v2.pdf
            p = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_FFFFFC2F
            a = 0
            b = 7
            x = 0x79BE667E_F9DCBBAC_55A06295_CE870B07_029BFCDB_2DCE28D9_59F2815B_16F81798
            y = 0x483ADA77_26A3C465_5DA4FBFC_0E1108A8_FD17B448_A6855419_9C47D08F_FB10D4B8
            q = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_BAAEDCE6_AF48A03B_BFD25E8C_D0364141
        elif t == 'secp256r1':
            # https://www.secg.org/sec2-v2.pdf
            p = 0xFFFFFFFF_00000001_00000000_00000000_00000000_FFFFFFFF_FFFFFFFF_FFFFFFFF
            a = 0xFFFFFFFF_00000001_00000000_00000000_00000000_FFFFFFFF_FFFFFFFF_FFFFFFFC
            b = 0x5AC635D8_AA3A93E7_B3EBBD55_769886BC_651D06B0_CC53B0F6_3BCE3C3E_27D2604B
            x = 0x6B17D1F2_E12C4247_F8BCE6E5_63A440F2_77037D81_2DEB33A0_F4A13945_D898C296
            y = 0x4FE342E2_FE1A7F9B_8EE7EB4A_7C0F9E16_2BCE3357_6B315ECE_CBB64068_37BF51F5
            q = 0xFFFFFFFF_00000000_FFFFFFFF_FFFFFFFF_BCE6FAAD_A7179E84_F3B9CAC2_FC632551
        elif t == 'secp384r1':
            # https://www.secg.org/sec2-v2.pdf
            p = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_FFFFFFFF_00000000_00000000_FFFFFFFF
            a = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_FFFFFFFF_00000000_00000000_FFFFFFFC
            b = 0xB3312FA7_E23EE7E4_988E056B_E3F82D19_181D9C6E_FE814112_0314088F_5013875A_C656398D_8A2ED19D_2A85C8ED_D3EC2AEF
            x = 0xAA87CA22_BE8B0537_8EB1C71E_F320AD74_6E1D3B62_8BA79B98_59F741E0_82542A38_5502F25D_BF55296C_3A545E38_72760AB7
            y = 0x3617DE4A_96262C6F_5D9E98BF_9292DC29_F8F41DBD_289A147C_E9DA3113_B5F0B8C0_0A60B1CE_1D7E819D_7A431D7C_90EA0E5F
            q = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_C7634D81_F4372DDF_581A0DB2_48B0A77A_ECEC196A_CCC52973
        elif t == 'secp521r1':
            # https://www.secg.org/sec2-v2.pdf
            p = 2 ** 521 - 1
            a = 2 ** 521 - 4
            b = 0x0051_953EB961_8E1C9A1F_929A21A0_B68540EE_A2DA725B_99B315F3_B8B48991_8EF109E1_56193951_EC7E937B_1652C0BD_3BB1BF07_3573DF88_3D2C34F1_EF451FD4_6B503F00
            x = 0x00C6_858E06B7_0404E9CD_9E3ECB66_2395B442_9C648139_053FB521_F828AF60_6B4D3DBA_A14B5E77_EFE75928_FE1DC127_A2FFA8DE_3348B3C1_856A429B_F97E7E31_C2E5BD66
            y = 0x0118_39296A78_9A3BC004_5C8A5FB4_2C7D1BD9_98F54449_579B4468_17AFBD17_273E662C_97EE7299_5EF42640_C550B901_3FAD0761_353C7086_A272C240_88BE9476_9FD16650
            q = 0x01FF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFA_51868783_BF2F966B_7FCC0148_F709A5D0_3BB5C9B8_899C47AE_BB6FB71E_91386409
        else:
            assert False
        return ECPoint(a, b, p, x, y, q = q)
    
    def __init__(self, A, B, N, x, y, *, q = 0, prepare = True):
        if prepare:
            N = self.Int(N)
            A, B, x, y, q = [self.Int(e) % N for e in [A, B, x, y, q]]
            assert (4 * A ** 3 + 27 * B ** 2) % N != 0
            assert (y ** 2 - x ** 3 - A * x - B) % N == 0, (hex(N), hex((y ** 2 - x ** 3 - A * x) % N))
            assert N % 4 == 3
            assert y == pow(x ** 3 + A * x + B, (N + 1) // 4, N)
        self.A, self.B, self.N, self.x, self.y, self.q = A, B, N, x, y, q
    
    def __add__(self, other):
        A, B, N = self.A, self.B, self.N
        Px, Py, Qx, Qy = self.x, self.y, other.x, other.y
        if Px == Qx and Py == Qy:
            s = ((Px * Px * 3 + A) * self.inv(Py * 2, N)) % N
        else:
            s = ((Py - Qy) * self.inv(Px - Qx, N)) % N
        x = (s * s - Px - Qx) % N
        y = (s * (Px - x) - Py) % N
        return ECPoint(A, B, N, x, y, prepare = False)
    
    def __rmul__(self, other):
        other = self.Int(other - 1)
        r = self
        while True:
            if other & 1:
                r = r + self
                if other == 1:
                    return r
            other >>= 1
            self = self + self
    
    @classmethod
    def inv(cls, a, n):
        a %= n
        if cls.gmpy2 is None:
            try:
                return pow(a, -1, n)
            except ValueError:
                import math
                raise cls.InvError(math.gcd(a, n), a, n)
        else:
            g, s, t = cls.gmpy2.gcdext(a, n)
            if g != 1:
                raise cls.InvError(g, a, n)
            return s % n

    def __repr__(self):
        return str(dict(x = self.x, y = self.y, A = self.A, B = self.B, N = self.N, q = self.q))

    def __eq__(self, other):
        for i, (a, b) in enumerate([(self.x, other.x), (self.y, other.y), (self.A, other.A),
                (self.B, other.B), (self.N, other.N), (self.q, other.q)]):
            if a != b:
                return False
        return True
        
def get_pub(priv_key):
    bp = ECPoint.std_point('secp256k1')
    pub = priv_key * bp
    return pub.x, pub.y

def main():
    import hashlib
    priv_key = int(hashlib.sha3_256(b" ").hexdigest(), 16)
    print('priv key :', hex(priv_key))
    pubx, puby = get_pub(priv_key)
    print('pub key x:', hex(pubx))
    print('pub key y:', hex(puby))

main()







