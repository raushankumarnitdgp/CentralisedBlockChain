# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:32:19 2020

@author: Raushan Kumar
"""

from secureserverlog import Blockchain

blockchain = Blockchain()

if (blockchain.is_chain_valid(blockchain.chain)):
    print("Valid BlockChain")
else:
    print("Tampered")