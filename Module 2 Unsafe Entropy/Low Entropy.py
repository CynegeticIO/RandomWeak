# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:21:08 2022

@author: CynegeticIO
"""

'''
To be secure against brute-force attacks, tokens need to have sufficient randomness. Unfortunately, what is considered sufficient will necessarily increase as computers get more powerful and able to make more guesses in a shorter period. As of 2015, it is believed that 32 bytes (256 bits) of randomness is sufficient for the typical use-case expected for the secrets module.

For those who want to manage their own token length, you can explicitly specify how much randomness is used for tokens by giving an int argument to the various token_* functions. That argument is taken as the number of bytes of randomness to use.

Otherwise, if no argument is provided, or if the argument is None, the token_* functions will use a reasonable default instead.
'''


'''
##################################################################################################################################
##################################################################################################################################

ENTROPY MOOD 1: Generate secure random numbers for managing secrets with random byte string containing nbytes number of bytes.
 
##################################################################################################################################
##################################################################################################################################
'''


import hashlib
from eth_keys import keys
from secrets import token_bytes, token_hex
from coincurve import PublicKey
from sha3 import keccak_256
import os 
import gc
import binascii
import pandas as pd

m = 100000
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

generated = pd.concat([adr_df, pk_df], axis=1)
generated = generated.sort_values(by= "Adr", ascending=True)
generated = generated.drop_duplicates()

generated.to_csv('LowEntropy_1.csv')



'''
##################################################################################################################################
##################################################################################################################################

ENTROPY MOOD 2: Generate secure random numbers for managing secrets with random byte string containing nbytes number of bytes.
 
##################################################################################################################################
##################################################################################################################################
'''

n = 1000000
adr = []
pk = []

for i in range(0,n):
    
    private_key = keccak_256(token_bytes(2)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    
    pk.append(str('0x'+private_key.hex()).lower())
    adr.append(str('0x'+addr.hex()).lower())
  
adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])

generated = pd.concat([adr_df, pk_df], axis=1)
generated = generated.sort_values(by= "Adr", ascending=True)
generated = generated.drop_duplicates()

generated.to_csv('LowEntropy_2.csv')

'''
##################################################################################################################################
##################################################################################################################################

ENTROPY MOOD 3: Generate secure random numbers for managing secrets with random byte string containing nbytes number of bytes.
 
##################################################################################################################################
##################################################################################################################################
'''

o = 10000000000
adr = []
pk = []

for i in range(0,o):
    
    private_key = keccak_256(token_bytes(3)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    
    pk.append(str('0x'+private_key.hex()).lower())
    adr.append(str('0x'+addr.hex()).lower())
  
adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])

generated = pd.concat([adr_df, pk_df], axis=1)
generated = generated.sort_values(by= "Adr", ascending=True)
generated = generated.drop_duplicates()

generated.to_csv('LowEntropy_3.csv')
