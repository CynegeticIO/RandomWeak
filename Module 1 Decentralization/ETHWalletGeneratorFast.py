# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:21:08 2022

@author: CynegeticIO
"""
import hashlib
from eth_keys import keys
from secrets import token_bytes, token_hex
from coincurve import PublicKey
from sha3 import keccak_256
import os 
import gc
import binascii
import pandas as pd

    
adr = []
pk = []

for i in range(0,1000000):
    
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    pk.append(str('0x'+private_key.hex()).lower())
    adr.append(str('0x'+addr.hex()).lower())
  
adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])



import sha3
from ecdsa import SigningKey, SECP256k1

keccak = sha3.keccak_256()
private = SigningKey.generate(curve=SECP256k1)
public = private.get_verifying_key().to_string()
keccak.update(public)
address = "0x{}".format(keccak.hexdigest()[24:])
print(address)
