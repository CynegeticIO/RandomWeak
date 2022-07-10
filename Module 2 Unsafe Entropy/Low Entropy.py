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

m = 1000000
adr = []
pk = []

for i in range(0,m):
    
    private_key = keccak_256(token_bytes(1)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    pk.append(str('0x'+private_key.hex()).lower())
    adr.append(str('0x'+addr.hex()).lower())
  
adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])

all_df = pd.concat([adr_df, pk_df], axis=1)

all_df.to_csv('20220710.csv')


