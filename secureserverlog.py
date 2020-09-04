# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:29:14 2020

@author: Raushan Kumar
"""
# Importing the libraries
import datetime
import hashlib
import json


class Blockchain:
    def __init__(self):
        with open("blockchain_file.json", "r", encoding='utf-8',errors='replace') as openfile: 
            json_arr = json.load(openfile)
        
        if not json_arr:
            self.chain = []
            self.create_block(previous_hash = '0', data='Genesis Block', filename='GenesisBlock.txt')
        else:
            self.chain = json_arr
            #print(self.chain)
            

    def find_valid_hash(self, index, timestamp, data, previous_hash):
        nonce = 1
        notvalid = True
        while(notvalid):
            block_data = str(index) + str(timestamp) + str(data) + str(previous_hash) + str(nonce)        #encoded_block = json.dumps(block, sort_keys = True).encode()
            hash_operation = hashlib.sha256(block_data.encode()).hexdigest()
            if hash_operation[:2] == '00':
                notvalid = False
            else:
                nonce += 1
        return hash_operation, nonce

    def create_block(self, previous_hash, data, filename):
        if self.is_chain_valid(self.chain):
            print("validated")
            index = len(self.chain)
            timestamp = str(datetime.datetime.now())
            curr_hash, nonce = self.find_valid_hash(index,timestamp, data, previous_hash)
            block = {'index': index,
                     'timestamp': timestamp,
                     'nonce': nonce,
                     'data': data,
                     'previous_hash': previous_hash,
                     'curr_hash': curr_hash,
                     'filename': filename
                     }
            self.chain.append(block)
            return block
        else:
            print("Invalid BlockChain")
            return -1
    

    def get_previous_block(self):
        return self.chain[-1]
    
    #need to improve
    def is_chain_valid(self, chain):
        if chain:
            previous_block = chain[0]
            block_index = 1
            while block_index < len(chain):
                block = chain[block_index]
                index = block['index']
                timestamp = block['timestamp']
                data = block['data']
                previous_hash = block['previous_hash']
                nonce = block['nonce']
                file_name = block['filename']
                with open(file_name, 'r', encoding='utf-8', errors='replace') as file:
                    file_data = file.read()
                block_data_blockchain = str(index) + str(timestamp) + str(data) + str(previous_hash) + str(nonce)        #encoded_block = json.dumps(block, sort_keys = True).encode()
                block_data_file = str(index) + str(timestamp) + str(file_data) + str(previous_hash) + str(nonce)
                hash_block1 = hashlib.sha256(block_data_blockchain.encode()).hexdigest()
                hash_block_file = hashlib.sha256(block_data_file.encode()).hexdigest()
                
                if block['curr_hash']!=hash_block_file:
                    print("Data of File "+file_name+" Block["+str(index)+"] tampered")
                    return False
                
                if block['curr_hash']!=hash_block1:
                    print("Data of File "+file_name+" Block["+str(index)+"] Block tampered in blockchain")
                    return False
                
                if block['previous_hash'] != previous_block['curr_hash']:
                    print("Previous hash of Block["+str(index)+"] doesnot matches")
                    return False
                
                previous_block = block
                block_index += 1
            return True
        return True
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    