# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:57:10 2022

@author: CynegeticIO
"""

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

import pandas as pd

adr = []
pk = []

for i in range(0,1000):
    
    kp = Keypair.generate()
    public_key = str(kp.public_key)
    secret_key = kp.secret_key.hex()
    pk.append(secret_key)
    adr.append(public_key)
    
adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])

