# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:42:02 2020

@author: Raushan Kumar
"""

from secureserverlog import Blockchain
import json

# Creating a Blockchain
blockchain = Blockchain()
previous_block = blockchain.get_previous_block()
#previous_block = json.loads(previous_block)
previous_hash = previous_block["curr_hash"]
file_name = input("Enter File Name to be added to blockchain ")
with open(file_name,  "r", encoding='utf-8',errors='replace') as file:
    data = file.read()
block = blockchain.create_block(previous_hash, data, file_name)
'''
print("93")
print(block)
'''
#json_block = json.dumps(block, sort_keys=True, indent=4)

'''
i = 0
while i < len(blockchain.chain):
    print(blockchain.chain[i])
    i = i+1
'''
print("Block Created")
if block!=-1:
    with open("blockchain_file.json", "w", encoding='utf-8',errors='replace') as write_file:
        json.dump(blockchain.chain, write_file,indent=4, separators=(", ", ": "), sort_keys=True)
  
