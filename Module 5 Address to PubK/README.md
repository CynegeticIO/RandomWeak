# KeyHunt-Cuda 
_Hunt for Bitcoin private keys._

This is a modified version of VanitySearch by [JeanLucPons](https://github.com/JeanLucPons/VanitySearch/).

Renamed from VanitySearch to KeyHunt (inspired from [keyhunt](https://github.com/albertobsd/keyhunt) by albertobsd).

A lot of gratitude to all the developers whose codes has been used here.

# Features
- For Bitcoin use ```--coin BTC``` and for Ethereum use ```--coin ETH```
- Single address(rmd160 hash) for BTC or ETH address searching with mode ```-m ADDREES```
- Multiple addresses(rmd160 hashes) or ETH addresses searching with mode ```-m ADDREESES```
- XPoint[s] mode is applicable for ```--coin BTC``` only
- Single xpoint searching with mode ```-m XPOINT```
- Multiple xpoint searching with mode ```-m XPOINTS```
- For XPoint[s] mode use x point of the public key, without 02 or 03 prefix(64 chars).
- Multiple addresses for both ETH and BTC and xpoints for BTC via cmd line.
- Cuda only.

# Usage
- For multiple addresses or xpoints, file format must be binary with sorted data.
- To convert Bitcoin addresses list(text format) to rmd160 hashes binary file use provided python script ```addresses_to_hash160.py```
- To convert pubkeys list(text format) to xpoints binary file use provided python script ```pubkeys_to_xpoint.py```
- To convert Ethereum addresses list(text format) to keccak160 hashes binary file use provided python script ```eth_addresses_to_bin.py```
- After getting binary files from python scripts, use ```BinSort``` tool provided with KeyHunt-Cuda to sort these binary files.
- Don't use XPoint[s] mode with ```uncompressed``` compression type.
- CPU and GPU can not be used together, because the program divides the whole input range into equal parts for all the threads, so use either CPU or GPU so that the whole range can increment by all the threads with consistency.
- Minimum entries for bloom filter is >= 2.

## addresses_to_hash160.py
```
python3 addresses_to_hash160.py addresses_in.txt hash160_out.bin
```

## pubkeys_to_xpoint.py
```
python3 pubkeys_to_xpoint.py pubkeys_in.txt xpoints_out.bin
```

## eth_addresses_to_bin.py
```
python3 eth_addresses_to_bin.py eth_addresses_in.txt eth_addresses_out.bin
```

## BinSort
For hash160 and keccak160 ```length``` is ```20``` and for xpoint ```length``` is ```32```.
```
BinSort.exe
Usage: BinSort.exe length in_file out_file
```

## KeyHunt-Cuda
```
KeyHunt-Cuda.exe -h
KeyHunt-Cuda [OPTIONS...] [TARGETS]
Where TARGETS is multiple address/xpont, or multiple hashes/xpoints file

-h, --help                               : Display this message
-c, --check                              : Check the working of the codes
-u, --uncomp                             : Search uncompressed points
-b, --both                               : Search both uncompressed or compressed points
-g, --gpu                                : Enable GPU calculation
--gpui GPU ids: 0,1,...                  : List of GPU(s) to use, default is 0
--gpux GPU gridsize: g0x,g0y,g1x,g1y,... : Specify GPU(s) kernel gridsize, default is 8*(Device MP count),128
-t, --thread N                           : Specify number of CPU thread, default is number of core
-i, --in FILE                            : Read rmd160 hashes or xpoints from FILE, should be in binary format with sorted
-o, --out FILE                           : Write keys to FILE, default: Found.txt
-m, --mode MODE                          : Specify search mode where MODE is
                                               ADDRESS  : for single address
                                               ADDRESSES: for multiple hashes/addresses
                                               XPOINT   : for single xpoint
                                               XPOINTS  : for multiple xpoints
--coin BTC/ETH                           : Specify Coin name to search
                                               BTC: available mode :-
                                                   ADDRESS, ADDRESSES, XPOINT, XPOINTS
                                               ETH: available mode :-
                                                   ADDRESS, ADDRESSES
-l, --list                               : List cuda enabled devices
--range KEYSPACE                         : Specify the range:
                                               START:END
                                               START:+COUNT
                                               START
                                               :END
                                               :+COUNT
                                               Where START, END, COUNT are in hex format
-r, --rkey Rkey                          : Random key interval in MegaKeys, default is disabled
-v, --version                            : Show version

```


CPU mode:
```
KeyHunt-Cuda.exe -t 4 --gpui 0 --gpux 256,256 -m addresses --coin BTC --range 1:1fffffffff -i puzzle_1_37_hash160_out_sorted.bin

KeyHunt-Cuda v1.07

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Multi Address
DEVICE       : CPU
CPU THREAD   : 4
SSE          : YES
RKEY         : 0 Mkeys
MAX FOUND    : 65536
HASH160 FILE : puzzle_1_37_hash160_out_sorted.bin
OUTPUT FILE  : Found.txt

Loaded       : 37 addresses

Bloom at 000001C84206BB70
  Version    : 2.1
  Entries    : 74
  Error      : 0.0000010000
  Bits       : 2127
  Bits/Elem  : 28.755175
  Bytes      : 266 (0 MB)
  Hash funcs : 20

Start Time   : Mon Jul 19 01:09:22 2021
Global start : 1 (1 bit)
Global end   : 1FFFFFFFFF (37 bit)
Global range : 1FFFFFFFFE (37 bit)


=================================================================================
PubAddress: 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU73sVHnoWn
Priv (HEX): 1
PubK (HEX): 0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
=================================================================================


=================================================================================
PubAddress: 1CUNEBjYrCn2y1SdiUMohaKUi4wpP326Lb
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU74sHUHy8S
Priv (HEX): 3
PubK (HEX): 02F9308A019258C31049344F85F89D5229B531C845836F99B08601F113BCE036F9
=================================================================================
[00:00:02] [CPU+GPU: 5.06 Mk/s] [GPU: 0.00 Mk/s] [C: 0.007474 %] [R: 0] [T: 10,272,768 (24 bit)] [F: 2]

....

```
```
KeyHunt-Cuda.exe -t 4 --gpui 0 --gpux 256,256 -m address --coin eth --range 8000000:fffffff 0xfda5c442e76a95f96c09782f1a15d3b58e32404f

KeyHunt-Cuda v1.07

COIN TYPE    : ETHEREUM
SEARCH MODE  : Single Address
DEVICE       : CPU
CPU THREAD   : 4
SSE          : NO
RKEY         : 0 Mkeys
MAX FOUND    : 65536
ETH ADDRESS  : 0xfda5c442e76a95f96c09782f1a15d3b58e32404f
OUTPUT FILE  : Found.txt

Start Time   : Fri Jul 23 01:32:59 2021
Global start : 8000000 (28 bit)
Global end   : FFFFFFF (28 bit)
Global range : 7FFFFFF (27 bit)


[00:00:32] [CPU+GPU: 3.19 Mk/s] [GPU: 0.00 Mk/s] [C: 77.716065 %] [R: 0] [T: 104,308,736 (27 bit)] [F: 0]
=================================================================================
PubAddress: 0xfda5c442e76a95f96c09782f1a15d3b58e32404f
Priv (HEX): D916CE8
PubK (HEX): E9E661838A96A65331637E2A3E948DC0756E5009E7CB5C36664D9B72DD18C0A709F531540A4CA59F50F93B8BF7B0C060045754AAAE7CE1BEA5A136C0D5874B97
=================================================================================
[00:00:34] [CPU+GPU: 3.19 Mk/s] [GPU: 0.00 Mk/s] [C: 82.519532 %] [R: 0] [T: 110,755,840 (27 bit)] [F: 1]

BYE
```


### GPU mode:
## Multiple addresses mode:
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m addresses --coin BTC -o Found.txt --range 1:1fffffffff -i puzzle_1_37_hash160_out_sorted.bin

KeyHunt-Cuda v1.07

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Multi Address
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : YES
RKEY         : 0 Mkeys
MAX FOUND    : 65536
HASH160 FILE : puzzle_1_37_hash160_out_sorted.bin
OUTPUT FILE  : Found.txt

Loaded       : 37 addresses

Bloom at 000001F0C78AAA40
  Version    : 2.1
  Entries    : 74
  Error      : 0.0000010000
  Bits       : 2127
  Bits/Elem  : 28.755175
  Bytes      : 266 (0 MB)
  Hash funcs : 20

Start Time   : Mon Jul 19 01:02:40 2021
Global start : 1 (1 bit)
Global end   : 1FFFFFFFFF (37 bit)
Global range : 1FFFFFFFFE (37 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)


=================================================================================
PubAddress: 1PgQVLmst3Z314JrQn5TNiys8Hc38TcXJu
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFUGxXgtm63M
Priv (HEX): 483
PubK (HEX): 038B05B0603ABD75B0C57489E451F811E1AFE54A8715045CDF4888333F3EBC6E8B
=================================================================================

=================================================================================
PubAddress: 1LeBZP5QCwwgXRtmVUvTVrraqPUokyLHqe
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFUBTL67V6dE
Priv (HEX): 202
PubK (HEX): 03A7A4C30291AC1DB24B4AB00C442AA832F7794B5A0959BEC6E8D7FEE802289DCD
=================================================================================

=================================================================================
PubAddress: 1CQFwcjw1dwhtkVWBttNLDtqL7ivBonGPV
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFUB3vfDKcxZ
Priv (HEX): 1D3
PubK (HEX): 0243601D61C836387485E9514AB5C8924DD2CFD466AF34AC95002727E1659D60F7
=================================================================================

....

```

## Multiple addresses mode with ethereum
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m addresses --coin eth --range 1:1fffffffff -i puzzle_1_37_addresses_eth_sorted.bin -o Found_Eth.txt

KeyHunt-Cuda v1.07

COIN TYPE    : ETHEREUM
SEARCH MODE  : Multi Address
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : NO
RKEY         : 0 Mkeys
MAX FOUND    : 65536
ETH ADDRESSES: puzzle_1_37_addresses_eth_sorted.bin
OUTPUT FILE  : Found_Eth.txt

Loaded       : 37 Ethereum addresses

Bloom at 00000231F97E6200
  Version    : 2.1
  Entries    : 74
  Error      : 0.0000010000
  Bits       : 2127
  Bits/Elem  : 28.755175
  Bytes      : 266 (0 MB)
  Hash funcs : 20

Start Time   : Fri Jul 23 01:36:50 2021
Global start : 1 (1 bit)
Global end   : 1FFFFFFFFF (37 bit)
Global range : 1FFFFFFFFE (37 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)


=================================================================================
PubAddress: 0x2c559fed4b8a8e12e170740d4dabb4fc7d3f9b49
Priv (HEX): 483
PubK (HEX): 8B05B0603ABD75B0C57489E451F811E1AFE54A8715045CDF4888333F3EBC6E8B1D10F88145DB40FB889E2DDCE81BDA7C27F5B615ACD6179DBB30F4FE7F40FB39
=================================================================================

=================================================================================
PubAddress: 0x86b1b106aeac5c5d2b16f9596755811cf976f34e
Priv (HEX): 202
PubK (HEX): A7A4C30291AC1DB24B4AB00C442AA832F7794B5A0959BEC6E8D7FEE802289DCDD580B4242CF68189AC1309E79C5A2132D2CBF0E18BE6D0B37D05A32256CA0C8B
=================================================================================

=================================================================================
PubAddress: 0xdba02a942650eb93cf2566dbcb7d945b9544afcd
Priv (HEX): 1460
PubK (HEX): AADAAAB1DB8D5D450B511789C37E7CFEB0EB8B3E61A57A34166C5EDC9A4B869D2ED7CAAF2A261616F564190B4BC9F496F3DF86353FF76D7F704E48E654BACDF1
=================================================================================
[00:00:02] [CPU+GPU: 265.02 Mk/s] [GPU: 265.02 Mk/s] [C: 0.390625 %] [R: 0] [T: 536,870,912 (30 bit)] [F: 13]
=================================================================================
PubAddress: 0x0fc0e54f047efb3fd041837213ecb572ad594263
Priv (HEX): 2930
PubK (HEX): B4F1DE58B8B41AFE9FD4E5FFBDAFAEAB86C5DB4769C15D6E6011AE7351E547597875EE3C7E4D1B5C753D3747C7D5774B583DA4D075FB8CAF8CAB311B0F350483
=================================================================================
...

```

## Single address mode
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m address --coin BTC --range 400000000:7ffffffff 1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb

KeyHunt-Cuda v1.07

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Single Address
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : YES
RKEY         : 0 Mkeys
MAX FOUND    : 65536
ADDRESS      : 1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb
OUTPUT FILE  : Found.txt

Start Time   : Mon Jul 19 01:08:06 2021
Global start : 400000000 (35 bit)
Global end   : 7FFFFFFFF (35 bit)
Global range : 3FFFFFFFF (34 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)

[00:00:24] [CPU+GPU: 368.81 Mk/s] [GPU: 368.81 Mk/s] [C: 54.687500 %] [R: 0] [T: 9,395,240,960 (34 bit)] [F: 0]
=================================================================================
PubAddress: 1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9MP7J9oTbu6KuRr
Priv (HEX): 4AED21170
PubK (HEX): 02F6A8148A62320E149CB15C544FE8A25AB483A0095D2280D03B8A00A7FEADA13D
=================================================================================
[00:00:26] [CPU+GPU: 360.62 Mk/s] [GPU: 360.62 Mk/s] [C: 58.593750 %] [R: 0] [T: 10,066,329,600 (34 bit)] [F: 1]

BYE
```

## Single address mode with ethereum
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m address --coin eth --range 800000000:fffffffff 0x1ffbb8f1dfc7e2308c39637e3f4b63c2362ddc6c

KeyHunt-Cuda v1.07

COIN TYPE    : ETHEREUM
SEARCH MODE  : Single Address
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : NO
RKEY         : 0 Mkeys
MAX FOUND    : 65536
ETH ADDRESS  : 0x1ffbb8f1dfc7e2308c39637e3f4b63c2362ddc6c
OUTPUT FILE  : Found.txt

Start Time   : Fri Jul 23 01:31:53 2021
Global start : 800000000 (36 bit)
Global end   : FFFFFFFFF (36 bit)
Global range : 7FFFFFFFF (35 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)

[00:00:49] [CPU+GPU: 262.44 Mk/s] [GPU: 262.44 Mk/s] [C: 37.109375 %] [R: 0] [T: 12,750,684,160 (34 bit)] [F: 0]
=================================================================================
PubAddress: 0x1ffbb8f1dfc7e2308c39637e3f4b63c2362ddc6c
Priv (HEX): AAAAAAAAA
PubK (HEX): 191E2BD4A789E873AFFA936C7F65AB7831C503556F7CF6753F190D5A1C4A91E046AC098E6ECCC7E0D380DE6F1A5748E1FC4FC515669A8AA084D25085392DA510
=================================================================================
[00:00:51] [CPU+GPU: 262.42 Mk/s] [GPU: 262.42 Mk/s] [C: 38.671875 %] [R: 0] [T: 13,287,555,072 (34 bit)] [F: 1]

BYE
```

## Multiple XPoints mode
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m xpoints --coin BTC --range 1:1fffffffff -i xpoints_1_37_out_sorted.bin

KeyHunt-Cuda v1.07

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Multi X Points
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : YES
RKEY         : 0 Mkeys
MAX FOUND    : 65536
XPOINTS FILE : xpoints_1_37_out_sorted.bin
OUTPUT FILE  : Found.txt

Loaded       : 37 xpoints

Bloom at 00000174E464AAF0
  Version    : 2.1
  Entries    : 74
  Error      : 0.0000010000
  Bits       : 2127
  Bits/Elem  : 28.755175
  Bytes      : 266 (0 MB)
  Hash funcs : 20

Start Time   : Mon Jul 19 01:13:05 2021
Global start : 1 (1 bit)
Global end   : 1FFFFFFFFF (37 bit)
Global range : 1FFFFFFFFE (37 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)


=================================================================================
PubAddress: 1PgQVLmst3Z314JrQn5TNiys8Hc38TcXJu
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFUGxXgtm63M
Priv (HEX): 483
PubK (HEX): 038B05B0603ABD75B0C57489E451F811E1AFE54A8715045CDF4888333F3EBC6E8B
=================================================================================

=================================================================================
PubAddress: 1LeBZP5QCwwgXRtmVUvTVrraqPUokyLHqe
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFUBTL67V6dE
Priv (HEX): 202
PubK (HEX): 03A7A4C30291AC1DB24B4AB00C442AA832F7794B5A0959BEC6E8D7FEE802289DCD
=================================================================================

...

```

## Single XPoint mode
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m xpoint --coin BTC --range 8000000000:ffffffffff a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4

KeyHunt-Cuda v1.07

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Single X Point
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : YES
RKEY         : 0 Mkeys
MAX FOUND    : 65536
XPOINT       : a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4
OUTPUT FILE  : Found.txt

Start Time   : Sun Jul 18 23:46:15 2021
Global start : 8000000000 (40 bit)
Global end   : FFFFFFFFFF (40 bit)
Global range : 7FFFFFFFFF (39 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)

[00:05:07] [CPU+GPU: 1012.98 Mk/s] [GPU: 1012.98 Mk/s] [C: 57.568359 %] [R: 0] [T: 316,485,402,624 (39 bit)] [F: 0]
=================================================================================
PubAddress: 1EeAxcprB2PpCnr34VfZdFrkUWuxyiNEFv
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9aFJuCJDo5F6Jm7
Priv (HEX): E9AE4933D6
PubK (HEX): 03A2EFA402FD5268400C77C20E574BA86409EDEDEE7C4020E4B9F0EDBEE53DE0D4
=================================================================================
[00:05:09] [CPU+GPU: 1006.20 Mk/s] [GPU: 1006.20 Mk/s] [C: 57.910156 %] [R: 0] [T: 318,364,450,816 (39 bit)] [F: 1]

BYE
```


## Multiple Addresses and XPoints via cmd line 
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m addresses --coin BTC --range 400000000:7ffffffff 1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb 17aeu2kjc6j4aL7Cq2RgWUYzFALyF4Jzq4

KeyHunt-Cuda v1.08

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Multi Address
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : YES
RKEY         : 0 Mkeys
MAX FOUND    : 65536
BTC ADDRESSES: Multiple Addresses via Cmdline
OUTPUT FILE  : Found.txt

Loaded       : 2 Bitcoin addresses

Bloom at 0000023A4F9B7410
  Version    : 2.1
  Entries    : 4
  Error      : 0.0000010000
  Bits       : 115
  Bits/Elem  : 28.755175
  Bytes      : 15 (0 MB)
  Hash funcs : 20

Start Time   : Wed Oct  6 10:36:51 2021
Global start : 400000000 (35 bit)
Global end   : 7FFFFFFFF (35 bit)
Global range : 3FFFFFFFF (34 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)

[00:00:26] [CPU+GPU: 337.67 Mk/s] [GPU: 337.67 Mk/s] [C: 52.343750 %] [R: 0] [T: 8,992,587,776 (34 bit)] [F: 0]
=================================================================================
PubAddress: 1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9MP7J9oTbu6KuRr
Priv (HEX): 4AED21170
PubK (HEX): 02F6A8148A62320E149CB15C544FE8A25AB483A0095D2280D03B8A00A7FEADA13D
=================================================================================
[00:00:30] [CPU+GPU: 329.95 Mk/s] [GPU: 329.95 Mk/s] [C: 60.156250 %] [R: 0] [T: 10,334,765,056 (34 bit)] [F: 1]
=================================================================================
PubAddress: 17aeu2kjc6j4aL7Cq2RgWUYzFALyF4Jzq4
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9MSNHu6VhxrnxmF
Priv (HEX): 5AED21170
PubK (HEX): 03F27539939EC8E4CDCC6F9EE17EBDC16231DD5ED6A34AE121F0519ADEE536F2EA
=================================================================================
[00:00:32] [CPU+GPU: 329.95 Mk/s] [GPU: 329.95 Mk/s] [C: 64.062500 %] [R: 0] [T: 11,005,853,696 (34 bit)] [F: 2]

BYE
```
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m address --coin eth --range 800000000:fffffffff 0x1ffbb8f1dfc7e2308c39637e3f4b63c2362ddc6c 0x8d01341c97905956d9a3b914aa62862318f4f2ac

KeyHunt-Cuda v1.08

COIN TYPE    : ETHEREUM
SEARCH MODE  : Multi Address
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : NO
RKEY         : 0 Mkeys
MAX FOUND    : 65536
ETH ADDRESSES: Multiple Addresses via Cmdline
OUTPUT FILE  : Found.txt

Loaded       : 2 Ethereum addresses

Bloom at 000002A91E076B90
  Version    : 2.1
  Entries    : 4
  Error      : 0.0000010000
  Bits       : 115
  Bits/Elem  : 28.755175
  Bytes      : 15 (0 MB)
  Hash funcs : 20

Start Time   : Wed Oct  6 10:24:01 2021
Global start : 800000000 (36 bit)
Global end   : FFFFFFFFF (36 bit)
Global range : 7FFFFFFFF (35 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)

[00:00:51] [CPU+GPU: 246.10 Mk/s] [GPU: 246.10 Mk/s] [C: 36.328125 %] [R: 0] [T: 12,482,248,704 (34 bit)] [F: 0]
=================================================================================
PubAddress: 0x1ffbb8f1dfc7e2308c39637e3f4b63c2362ddc6c
Priv (HEX): AAAAAAAAA
PubK (HEX): 191E2BD4A789E873AFFA936C7F65AB7831C503556F7CF6753F190D5A1C4A91E046AC098E6ECCC7E0D380DE6F1A5748E1FC4FC515669A8AA084D25085392DA510
=================================================================================
[00:01:13] [CPU+GPU: 246.18 Mk/s] [GPU: 246.18 Mk/s] [C: 52.343750 %] [R: 0] [T: 17,985,175,552 (35 bit)] [F: 1]
=================================================================================
PubAddress: 0x8d01341c97905956d9a3b914aa62862318f4f2ac
Priv (HEX): BBBBBBBBB
PubK (HEX): EBA94B484686BF530BDDFD2C0278346723238D26CEA868422F355862639CEA863AC8D1181FB7116797AAFD3FC68846D9850C9480F0F5C2191A1716F56554308F
=================================================================================
[00:01:15] [CPU+GPU: 245.97 Mk/s] [GPU: 245.97 Mk/s] [C: 53.906250 %] [R: 0] [T: 18,522,046,464 (35 bit)] [F: 2]

BYE
```
```
KeyHunt-Cuda.exe -t 0 -g --gpui 0 --gpux 256,256 -m xpoints --coin BTC --range 400000000:7ffffffff 02F6A8148A62320E149CB15C544FE8A25AB483A0095D2280D03B8A00A7FEADA13D 03F27539939EC8E4CDCC6F9EE17EBDC16231DD5ED6A34AE121F0519ADEE536F2EA

KeyHunt-Cuda v1.08

COMP MODE    : COMPRESSED
COIN TYPE    : BITCOIN
SEARCH MODE  : Multi X Points
DEVICE       : GPU
CPU THREAD   : 0
GPU IDS      : 0
GPU GRIDSIZE : 256x256
SSE          : NO
RKEY         : 0 Mkeys
MAX FOUND    : 65536
BTC XPOINTS  : Multiple Xpoints via Cmdline
OUTPUT FILE  : Found.txt

Loaded       : 2 Bitcoin xpoints

Bloom at 00000204794877D0
  Version    : 2.1
  Entries    : 4
  Error      : 0.0000010000
  Bits       : 115
  Bits/Elem  : 28.755175
  Bytes      : 15 (0 MB)
  Hash funcs : 20

Start Time   : Wed Oct  6 10:22:48 2021
Global start : 400000000 (35 bit)
Global end   : 7FFFFFFFF (35 bit)
Global range : 3FFFFFFFF (34 bit)

GPU          : GPU #0 GeForce GTX 1650 (14x64 cores) Grid(256x256)

[00:00:08] [CPU+GPU: 987.31 Mk/s] [GPU: 987.31 Mk/s] [C: 46.875000 %] [R: 0] [T: 8,053,063,680 (33 bit)] [F: 0]
=================================================================================
PubAddress: 1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9MP7J9oTbu6KuRr
Priv (HEX): 4AED21170
PubK (HEX): 02F6A8148A62320E149CB15C544FE8A25AB483A0095D2280D03B8A00A7FEADA13D
=================================================================================
[00:00:10] [CPU+GPU: 986.88 Mk/s] [GPU: 986.88 Mk/s] [C: 58.593750 %] [R: 0] [T: 10,066,329,600 (34 bit)] [F: 1]
=================================================================================
PubAddress: 17aeu2kjc6j4aL7Cq2RgWUYzFALyF4Jzq4
Priv (WIF): p2pkh:KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9MSNHu6VhxrnxmF
Priv (HEX): 5AED21170
PubK (HEX): 03F27539939EC8E4CDCC6F9EE17EBDC16231DD5ED6A34AE121F0519ADEE536F2EA
=================================================================================
[00:00:12] [CPU+GPU: 975.54 Mk/s] [GPU: 975.54 Mk/s] [C: 69.531250 %] [R: 0] [T: 11,945,377,792 (34 bit)] [F: 2]

BYE
```

## Building
##### Windows
- Microsoft Visual Studio Community 2019 
- CUDA version 10.0
##### Linux
 - Edit the makefile and set up the appropriate CUDA SDK and compiler paths for nvcc. Or pass them as variables to `make` command.
 - Install libgmp: ```sudo apt install -y libgmp-dev```

    ```make
    CUDA       = /usr/local/cuda-11.0
    CXXCUDA    = /usr/bin/g++
    ```
 - To build CPU-only version (without CUDA support):
    ```sh
    $ make all
    ```
 - To build with CUDA: pass CCAP value according to your GPU compute capability
 - To get info about various Nvidia GPU CCAP value see [this](https://arnon.dk/matching-sm-architectures-arch-and-gencode-for-various-nvidia-cards/).
    ```sh
    $ cd KeyHunt-Cuda
    $ make gpu=1 CCAP=75 all
    ```
#### BinSort
```sh
$ cd BinSort
$ make
```
#### Python scripts
```
python3 -m pip install base58
```

## License
KeyHunt-Cuda is licensed under GPLv3.

## Donation
- BTC: bc1qwnd4jqe0ulldr7rn8dk8mpkytm7jz068mpau9w
- ETH: 0x16DD2B876C91d168cBAF7c18b78b9d0aDc011365

## __Disclaimer__
ALL THE CODES, PROGRAM AND INFORMATION ARE FOR EDUCATIONAL PURPOSES ONLY. USE IT AT YOUR OWN RISK. THE DEVELOPER WILL NOT BE RESPONSIBLE FOR ANY LOSS, DAMAGE OR CLAIM ARISING FROM USING THIS PROGRAM.


# Pollard-Kangaroo

Pollard, kangaroo method, solving discrete logarithm problem (DLP) using pseudorandom walks.
Its the kangaroo method (of [11, p. 13]) using distinguished points.
Runtime expected of 2w<sup>1/2</sup> group operations.

[11] P. C. van Oorschot and M. J. Wiener, Parallel collision search with cryptanalytic applications, J. Cryptology, #12 (1999)

# Feature:

 - singlecore, multicore
 - python2/3 compatibility (print/time/input/xrange/IntDiv)
 - auto adaptation under environment
 - raw python/coincurve+cffi/gmpy2
 - some checks, debug, more info, minor accelerate
 - (un)compress/custom/random pubkey
 - format time: 0y 0m 0d 00:00:00s 000ms
 - format prefix SI: Kilo/Mega/Giga/Tera/Peta/Exa
 - heuristic prognosis (avg)time and (avg)jump per bits
 - repair kangaroos, that falls into the trap of same sequences
 - location privkey in keyspace on the strip
 - percent status progress, lost/left time
 - support arbitrary range (keyspace) start:end
 - profiles settings/algorithms

Expected in the future
 - named argv
 - precision S(i) set without problem of odd of pow2
 - <s>neural network for user entertainment speaking in the voice of Jarvis</s> or anything else

Multicore options:
 1) naive parallelism, split equally the search range
 2) parallelism by Oorschot&Wiener
 - has problem of collisions between members of the same herd
 3) parallelism by Pollard (best choice)
 - coprime/odd numbers U=V=2p+/-1, U+V<=Ncores
 - without problem of collisions between members of the same herd
 
*Acceleration on several devices (i.e. with shared RAM) for 2) and 3) (w<sup>1/2</sup>/Ncores) can only be achieved using the pool.
Filtered distinguished points should be sent to the pool in a single hashtable.

*removed support coincurve lib, reason: if u can install coincurve - that u can install gmpy2

# Compilation

Its python implementation, need install python 2 or 3.

Raw python is more x10 slower, recommended install module gmpy2.

how to install gmpy2 on windows
 1) download file .whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/
 2) put to root dir of python
 3) install as:
 
Python27>python -m pip install gmpy2-2.0.8-cp27-cp27m-win_amd64.whl

Python37>python -m pip install gmpy2-2.0.8-cp37-cp37m-win_amd64.whl

# Benchmark libs
Algo: 1 Tame + 1 Wild with distinguished points,  expected of 2w<sup>1/2</sup> group operations

1core i5-2540, win7x64, python2x64
```
[lib#raw]		 7.1K j/s
[lib#coincurve]		24.5K j/s
[lib#coincurve+cffi]	35.4K j/s
[lib#gmpy2]		89.4K j/s
```

1core i5-2540, win7x64, python3x64
```
[lib#raw]		 8.9K j/s
[lib#coincurve]		31.2K j/s
[lib#coincurve+cffi]	43.2K j/s
[lib#gmpy2]		97.8K j/s
```

# Heuristic prognose
Algo: 1 Tame + 1 Wild with distinguished points,  expected of 2w<sup>1/2</sup> group operations

avg stat after 100tests

1core i5-2540, python37x64 + gmpy2, win7x64

[i] 97.8K j/s;..

|   W   |jump avg/2w^(1/2)| time                         avg/2w^(1/2)                         |
|:-----:|:---------------:|:-----------------------------------------------------------------:|
| 2^020 |    1.8K/   2.0K |              0d 00:00:00s 018ms /              0d 00:00:00s 020ms |
| 2^030 |   57.3K/  65.5K |              0d 00:00:00s 586ms /              0d 00:00:00s 670ms |
|>2^031 |   81.1K/  92.7K |              0d 00:00:00s 829ms /              0d 00:00:00s 948ms |
| 2^032 |  114.6K/ 131.1K |              0d 00:00:01s 173ms /              0d 00:00:01s 341ms |
| 2^040 |    1.8M/   2.1M |              0d 00:00:18s 777ms /              0d 00:00:21s 471ms |
| 2^050 |   58.7M/  67.1M |              0d 00:10:00s 886ms /              0d 00:11:27s 086ms |
| 2^060 |    1.9G/   2.1G |              0d 05:20:28s 355ms /              0d 06:06:26s 759ms |
| 2^070 |   60.1G/  68.7G |              7d 02:55:07s 378ms /              8d 03:26:16s 292ms |
| 2^080 |    1.9T/   2.2T |          7m 17d 21:23:56s 096ms /          8m 20d 14:00:41s 355ms |
| 2^090 |   61.5T/  70.4T |     20y  3m  2d 12:45:55s 095ms /     23y  1m 28d 16:22:03s 390ms |
| 2^100 |    2.0P/   2.3P |    648y  2m 21d 00:29:23s 067ms /    741y  2m 17d 19:45:48s 481ms |
| 2^105 |   11.1P/  12.7P |   3.7Ky 10m 29d 06:43:07s 581ms /   4.2Ky 11m 12d 16:12:57s 514ms |
| 2^110 |   63.0P/  72.1P |  20.7Ky  2m 12d 15:40:18s 166ms /  23.7Ky 11m  0d 08:25:51s 416ms |
| 2^120 |    2.0E/   2.3E | 663.8Ky  5m 14d 21:29:41s 312ms / 759.0Ky  4m 11d 05:47:25s 328ms |


# Discussion
more info

https://bitcointalk.org/index.php?topic=5173445.msg52473992#msg52473992

https://bitcointalk.org/index.php?topic=5166284.msg52318676#msg52318676

# How pollard-kangaroo works, the Tame and Wild kangaroos, is a simple explanation.

Suppose there is pubkeyX, unknow privkeyX, but privkeyX is in range w=[L..U]. 
The keys have a property - if we increase pubkey by S, then its privkey will also increase by S. 
We start step-by-step to increase pubkeyX by S(i), keeping sumX(S(i)). This is a Wild kangaroo. 
We select a random privkeyT from range [L..U], compute pubkeyT. 
We start step-by-step to increment pubkeyT by S(i) while maintaining sumT(S(i)). This is a Tame kangaroo. 
The size of the jump S(i) is determined by the x coordinate of the current point, so if a Wild or Tame kangaroo lands on one point, their paths will merge. 
(we are concerned with pseudo random walks whose next step is determined by the current position) 
Thanks to the Birthday Paradox (Kruskal's card trick), their paths will one day meet. 
Knowing each traveled path (sumX and sumT), privkeyX is calculated. 
The number of jumps is approximately 2w<sup>1/2</sup> group operations, which is much less than a full search w. 

# Articles

base
https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/

hand translate to ru/ua (recommend instead translate.google)
https://habr.com/ru/post/335906/


- [1] Best of the best, all in 1, epic,  2012

Chapter 14. Factoring and Discrete Logarithms using Pseudorandom Walks 
https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch14.pdf

- [2] with reference to old

J. M. Pollard, “Kangaroos, monopoly and discrete logarithms,” Journal of Cryptology, #13 (2000) 
https://web.northeastern.edu/seigen/11Magic/KruskalsCount/PollardKangarooMonopoly.pdf

(good dir web.northeastern.edu/seigen/11Magic/KruskalsCount/)

- [3] About parallelism problems

P. C. van Oorschot and M. J. Wiener, Parallel collision search with cryptanalytic applications, J. Cryptology, #12 (1999) 
https://people.scs.carleton.ca/~paulv/papers/JoC97.pdf