# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:25:03 2022

@author: CynegeticIO
"""

'''
Experiment to Replicate

https://www.ise.io/casestudies/ethercombing/

'''
m = 1000000
pk = []
adr = []

import hashlib
from eth_keys import keys
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import os 
import gc
import binascii
import pandas as pd


for i in range(0,m):
    
    n = str(hex(i))
    # 64 0s
    k = str("0000000000000000000000000000000000000000000000000000000000000000")+n[2:]
    k_v = k[-64:]
    pk.append("0x" + k_v)
    
    
    

for i in range(0,m):
    
    n = hex(i)
    # 64 0s
    k = n[2:]
    pk.append(k)
    
    
    
for j in range(0,m):

    private_key = binascii.hexlify(token_bytes(1)).hex()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    adr.append(str('0x'+addr.hex()).lower())
    
    
for i in range(0,72000):
    
    private_key = keccak_256(token_bytes(1)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    pk.append(str('0x'+private_key.hex()).lower())
    adr.append(str('0x'+addr.hex()).lower())
  
adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])

all_df = pd.concat([adr_df, pk_df], axis=1)

all_df.to_csv('20220710.csv')










