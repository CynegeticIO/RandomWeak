# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:17:35 2022

@author: CynegeticIO
"""

import requests
from bipwallet import wallet
from bipwallet.utils import *
from threading import Thread


for i in range(5):
    wgm = wallet.generate_mnemonic()
    master_key = HDPrivateKey.master_key_from_mnemonic(wgm)
    root_keys = HDKey.from_path(master_key,"m/44'/60'/0'")
    acct_priv_key = root_keys[-1]
    keys = HDKey.from_path(acct_priv_key,'{change}/{index}'.format(change=0, index=i))
    private_key = keys[-1]
    public_key = private_key.public_key
    print("Mnemonic: " + wgm)
    print("Private key: " + private_key._key.to_hex())
    print("Address: " + private_key.public_key.address())
    
