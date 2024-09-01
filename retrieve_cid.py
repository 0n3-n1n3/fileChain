import json
import os
import sys

def get_cid_from_blockchain(hash_value):
    file_path = 'blockchain_data.json'
    if not os.path.exists(file_path):
        return "Blockchain data file not found."

    try:
        with open(file_path, 'r') as f:
            blockchain = json.load(f)
    except json.JSONDecodeError:
        return "Error decoding blockchain data."

    for block in blockchain['chain']:
        if block['hash'] == hash_value:
            return block['cid']
    return "CID not found for the provided hash."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python retrieve_cid.py <hash>")
        sys.exit(1)
    
    hash_value = sys.argv[1]
    cid = get_cid_from_blockchain(hash_value)
    print(cid)

