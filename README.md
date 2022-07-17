# RandomWeak Project

## Description 

### Module 1

The idea of this repository is that anyone will be able to create an Ethereum, Avalanche, Arbitrum, BSC, Fantom or Polygon address either by uniquely creating their private key without having derived the mnemonic or by generating the mnemonic for later derivation.

After creating your Ethereum address you will be able to import it into Metamask, TrustWallet or any Wallet that you prefer, to start working with your new self-created address.

### Module 2

The project starts by contemplating the random generation of different weak entropies that may entrain common features in different methods in the creation of Private Keys for the different networks in the BlockChain.

### Module 3

This module mainly consists in being able to develop faster and faster tools to try to detect collisions in the different addresses of ETH and its compatible networks. We are making a lot of noticeable progress in speed. Where in a first phase with CPU we were able to scan approximately 70.000 keys/second we have just reached the record of 1.250.000 keys/second.

## Getting Started

### How to generate a Wallet?

<img src="https://img2.helpnetsecurity.com/posts2019/ise-042019-1.jpg" width="512"/>

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

```py
[+] Starting CynegeticIO Collisions...........................Wait........................
Starting thread: 4 base:  0x4ed61f80a90bcc2d536e6f498482abda5e6559bbc415b88251e1201539fd319a
Starting thread: 3 base:  0xe9025bd268958b810f01edb5512705c7dc8a351a64eb787ae76502801802a730
Starting thread: 1 base:  0x1b3c64683d32c2048e538741d9bc4149d9709f0ddae9f0d6a5fe1344e81cc37
Starting thread: 0 base:  0x82ca964195e9330d3a67e9634e4dd2929f1b81d2b9ce010c992437dc1284752a
Starting thread: 6 base:  0x23e56baef97563686cdc98b58488706adcb767d001bf189a4c77617894e42a9b
Starting thread: 5 base:  0x90c25326faad1a98fbde67dec31f0f559225d551156ec9bf5600b73a9f67880
Starting thread: 2 base:  0x886b14239cf99f967109606f6ad09817eefe3ccc9154f542fb399055b002dc2e
Starting thread: 7 base:  0x2e6ba08162a336ba5d7e53d97078546e9f086c5fac2e548433dd35459b3dc4b4
[+] Total Keys Checked : 1244000000  [ Speed : 1253356.29 Keys/s ]  Current ETH: 0x6380e66f6047fdc7b23e5adc036d4e2282e100ac
[+] Total Keys Checked : 1245000000  [ Speed : 1254193.68 Keys/s ]  Current ETH: 0x2e8ae9484cac6e89a29b701fecb272f8eabdefd7
[+] Total Keys Checked : 1246000000  [ Speed : 1254193.00 Keys/s ]  Current ETH: 0xf9b1fba030f297b66495e3eeef3486173c7ece4f
[+] Total Keys Checked : 1247000000  [ Speed : 1253777.29 Keys/s ]  Current ETH: 0xec9e27eb7114983701288a0a58a3b142486a04d3
[+] Total Keys Checked : 1248000000  [ Speed : 1254562.57 Keys/s ]  Current ETH: 0x858c21dcd0c79734d4f104d45ab6881d7ee2d171
[+] Total Keys Checked : 1249000000  [ Speed : 1254869.58 Keys/s ]  Current ETH: 0x1394645d01c28d5a899ea97f7154bc5639cb42eb
[+] Total Keys Checked : 1250000000  [ Speed : 1253921.75 Keys/s ]  Current ETH: 0x6d71850b2414b34de98307f7e4b51995421780ec
[+] Total Keys Checked : 1251000000  [ Speed : 1253873.65 Keys/s ]  Current ETH: 0xe8cc239ed2001f90d5158c0fa458aa626b713e87
[+] Total Keys Checked : 1252000000  [ Speed : 1253337.43 Keys/s ]  Current ETH: 0x04ed4e073dfaa2da59167b398184646ab8ffe0e6
[+] Total Keys Checked : 1252000000  [ Speed : 1253062.81 Keys/s ]  Current ETH: 0x4902633027bd1b75703fa87f1630e552814fe8fb
[+] Total Keys Checked : 1254000000  [ Speed : 1254014.31 Keys/s ]  Current ETH: 0x7bca1912acd6a25f28501bb95f979f07ea90bde8
[+] Total Keys Checked : 1255000000  [ Speed : 1253476.64 Keys/s ]  Current ETH: 0x7ae0b600b4e0d4b0baeb4fe4ff3ef4fae4e10489
[+] Total Keys Checked : 1256000000  [ Speed : 1254084.42 Keys/s ]  Current ETH: 0xe1779a4e00cba70ec386fae17336f31587fd8156
[+] Total Keys Checked : 1257000000  [ Speed : 1254671.83 Keys/s ]  Current ETH: 0x8008ee4afab77f2ed636646d008c37ce42eacf21
```

## Authors
  
[@CynegeticIO](https://twitter.com/CynegeticIO)
[@CY0xF](https://github.com/CY0xF)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Contact

@CY0xF - [@CynegeticIO](https://twitter.com/CynegeticIO) - team@cynegetic.io

Project Link: [https://github.com/BetaShelley/RandomWeak](https://github.com/BetaShelley/RandomWeak)


## Acknowledgments

Inspiration by:

* [ISE Ethercombing](https://www.ise.io/casestudies/ethercombing/)
* [Arthur Koziel](https://www.arthurkoziel.com/generating-ethereum-addresses-in-python/)
* [SECP256k1](https://en.bitcoin.it/wiki/Secp256k1)
* [SHA-256 Online Tool](https://emn178.github.io/online-tools/sha256.html)
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

<p align="right">(<a href="#top">back to top</a>)</p>
