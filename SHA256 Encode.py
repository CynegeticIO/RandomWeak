# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:25:03 2022

@author: CynegeticIO
"""

import hashlib

str_x = "ACDC"

hashedval = hashlib.sha256(str_x.encode())
print(hashedval)
hashedval.hexdigest()





