# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:25:03 2022

@author: CynegeticIO
"""

'''
Webs to Scrap

https://etherscan.io/accounts
https://snowtrace.io/accounts
https://ftmscan.com/accounts
https://polygonscan.com/accounts
https://arbiscan.io/accounts
https://bscscan.com/accounts
https://moonriver.moonscan.io/
https://optimistic.etherscan.io/
https://celoscan.io/

'''

import requests
import pandas as pd
from bs4 import BeautifulSoup


dfs = []
for page in range(1, 11):
    url = f"https://www.eliteprospects.com/league/nhl/stats/2021-2022?sort=tp&page={page}"
    print(f"Loading {url=}")
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    df = (
        pd.read_html(str(soup.select_one(".player-stats")))[0]
        .dropna(how="all")
        .reset_index(drop=True)
    )
    dfs.append(df)

df_final = pd.concat(dfs).reset_index(drop=True)
print(df_final)
df_final.to_csv("data.csv", index=False)





