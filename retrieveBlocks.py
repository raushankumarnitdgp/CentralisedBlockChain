# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:56:08 2020

@author: Raushan Kumar
"""
from datetime import datetime
from secureserverlog import Blockchain
import json


blockchain = Blockchain()

print("Enter time interval to retrive blocks between it")
ldate = input("Enter First Date/Time  ")
rdate = input("Enter Second Date/Time ")
ldate = datetime.strptime(ldate,'%Y-%m-%d')
rdate = datetime.strptime(rdate,'%Y-%m-%d')
blocks = []
i=0
while(i<len(blockchain.chain)):
    if (datetime.strptime(blockchain.chain[i]['timestamp'][:10],'%Y-%m-%d')>=ldate and datetime.strptime(blockchain.chain[i]['timestamp'][:10],'%Y-%m-%d')<=rdate):
        blocks.append(blockchain.chain[i])
    i = i+1

with open("retrievedBlockChain_file.json", "w", encoding='utf-8',errors='replace') as write_file:
        json.dump(blocks, write_file,indent=4, separators=(", ", ": "), sort_keys=True)
