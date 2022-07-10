# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:20:17 2022

@author: CynegeticIO
"""

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
import pandas as pd

adr = []
pk = []
mmn =[]

for i in range(0,5):
    # Generate english mnemonic words
    MNEMONIC: str = generate_mnemonic(language="english", strength=128)
    # Secret passphrase/password for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"
    # Initialize Ethereum mainnet BIP44HDWallet
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    # Get Ethereum BIP44HDWallet from mnemonic
    bip44_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE)
    # Clean default BIP44 derivation indexes/paths
    bip44_hdwallet.clean_derivation()
    #print("Mnemonic:", bip44_hdwallet.mnemonic())
    mmn.append(bip44_hdwallet.mnemonic())
    # Derivation from Ethereum BIP44 derivation path
    bip44_derivation: BIP44Derivation = BIP44Derivation(cryptocurrency=EthereumMainnet, account=0, change=False, address=0)
    # Drive Ethereum BIP44HDWallet
    bip44_hdwallet.from_path(path=bip44_derivation)
    adr.append(bip44_hdwallet.address().lower())
    pk.append("0x"+bip44_hdwallet.private_key().lower())
    # Clean derivation indexes/paths
    bip44_hdwallet.clean_derivation()

adr_df = pd.DataFrame(adr,columns=["Adr"])
pk_df = pd.DataFrame(pk,columns=["Pk"])
mmn_df = pd.DataFrame(mmn,columns=["MMN"])
