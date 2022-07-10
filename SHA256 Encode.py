# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:25:03 2022

@author: CynegeticIO

IMPORTANT LINKS:
    
    https://weakpass.com/
    https://web.archive.org/web/20120207113205/http://www.insidepro.com/eng/download.shtml
    
"""


import hashlib

str_x = "ACDC"

hashedval = hashlib.sha256(str_x.encode())
print(hashedval)
hashedval.hexdigest()





