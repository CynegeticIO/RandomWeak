# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:25:03 2022

@author: CynegeticIO
"""

'''
Experiment to Replicate

https://www.ise.io/casestudies/ethercombing/

'''


import hashlib
from eth_keys import keys
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import os 
import gc
import binascii
import pandas as pd

m = 1000000
pk = []
adr = []

for i in range(0,m):
    
    n = str(hex(i))
    # 64 0s
    k = str("0000000000000000000000000000000000000000000000000000000000000000")+n[2:]
    k_v = k[-64:]
    pk.append("0x" + k_v)

m = 1000000
pk = []
adr = []
    
for i in range(0,m):
    
    n = hex(i)
    # 64 0s
    k = n[2:]
    pk.append(k)
    
m = 1000000
pk = []
adr = []












