# RandomWeak
The project starts by contemplating the random generation of different weak entropies that may entrain common features in different methods in the creation of Private Keys for the different networks in the BlockChain.

# WalletGenerator

<img src="https://img2.helpnetsecurity.com/posts2019/ise-042019-1.jpg" width="512"/>

## Description

The idea of this repository is that anyone will be able to create an Ethereum, Avalanche, Arbitrum, BSC, Fantom or Polygon address either by uniquely creating their private key without having derived the mnemonic or by generating the mnemonic for later derivation.

After creating your Ethereum address you will be able to import it into Metamask, TrustWallet or any Wallet that you prefer, to start working with your new self-created address.

## Getting Started

### What do you Need?

* Python 3.9

* Any IDE Python (Spyder, PyCharm, KDevelop, SlickEdit ...)

### Installing Dependences

```bash
> pip install pysha3 ethereum hdwallet bipwallet two1 pycrypto rlp pycryptodome solana
```

```py
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

## STEP 1: GENERATE A PRIVATE KEY ##
#----------------------------------#
# Ethereum private keys are based on KECCAK-256 hashes (https://keccak.team/keccak.html).
# To generate such a hash we use the `keccak_256` function 
# from the `pysha3` module on a random 32 byte seed:

private_key = keccak_256(token_bytes(32)).digest()

## STEP 2: DERIVE THE PUBLIC KEY FROM THE PRIVATE KEY ##
#------------------------------------------------------#
# To get our public key we need to sign our private key with an
# Elliptic Curve Digital Signature Algorithm (ECDSA).
# Ethereum uses the `secp256k1` curve ECDSA. 
# `coincurve` uses this as a default so we don't need to 
# explicitly specify it when calling the function:

public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]

# The Ethereum Yellow Paper (https://ethereum.github.io/yellowpaper/paper.pdf)
# states that the public key has to be a byte array of size 64. By default 
# `coincurve` uses the compressed format for public keys (`libsecp256k1` 
# was developed for Bitcoin, where compressed keys are commonly used) 
# which is 33 bytes in size. Uncompressed keys are 65 bytes in size.
# Additionally all public keys are prepended with a single byte to indicate
# if they are compressed or uncompressed. This means we first need to get
# the uncompressed 65 byte key (`compressed=False`) and then strip the 
# first byte (`[1:]`) to get our 64 byte Ethereum public key.

## STEP 3: DERIVE THE ETHEREUM ADDRESS FROM THE PUBLIC KEY ##
#-----------------------------------------------------------#
# As specified in the Ethereum Yellow Paper (https://ethereum.github.io/yellowpaper/paper.pdf)
# we take the right most 20 bytes of the 32 byte `KECCAK` hash of the 
# corresponding ECDSA public key.

addr = keccak_256(public_key).digest()[-20:]

print('private_key:', private_key.hex())
print('eth addr: 0x' + addr.hex())
```


## Authors
  
[@CynegeticIO](https://twitter.com/CynegeticIO)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

[![card](https://github-readme-stats.vercel.app/api?username=CynegeticIO&theme=default&show_icons=true)](https://github.com/BetaShelley/RandomWeak)

## Contact

Cynio - [@CynegeticIO](https://twitter.com/CynegeticIO) - team@cynegetic.io

Project Link: [https://github.com/CynegeticIO/WalletGenerator](https://github.com/CynegeticIO/WalletGenerator)


## Acknowledgments

Inspiration by:

* [Vanity-C++](https://github.com/johguse/profanity)
* [Vanity-Rust](https://rustrepo.com/repo/Limeth-ethaddrgen-rust-cryptography)
* [Vanity-JavaScript](https://github.com/MyEtherWallet/VanityEth)
* [BIP44 Standard Idea](https://github.com/michailbrynard/ethereum-bip44-python)
* [Origin Idea for BTC](https://github.com/21dotco/two1-python/tree/master/two1)


# Thanks The Consideration

Any support is deeply appreciated.
Crypto currencies have the lowest fees.

## Crypto Currency Wallets Recieving Donations

> BTC:  `bc1qnr97mmekqw5z4dgrd8v6pclpstt6jjnf63zmff`

> ETH:  `0xfdc39e84f80a6ae1fd9d1f4acf22ee527ab85de9`

<p align="right">(<a href="#top">back to top</a>)</p>
