import os
import requests
from dotenv import load_dotenv
from blockchain import Blockchain

load_dotenv()

IPFS_API_URL = 'http://localhost:5001/api/v0'
jwt_token = os.getenv('PINATA_JWT_TOKEN')

def upload_to_ipfs(filename):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {'Authorization': f'Bearer {jwt_token}'}
    with open(filename, 'rb') as file:
        response = requests.post(url, files={'file': file}, headers=headers)
        response.raise_for_status()
        return response.json()

def get_cid(filename):
    response = upload_to_ipfs(filename)
    return response.get('IpfsHash')

def add_to_blockchain(filename):
    bc = Blockchain()
    cid = get_cid(filename)
    if cid:
        blockchain_hash = bc.new_block(cid)
        return blockchain_hash
    else:
        raise Exception("Failed to get CID from IPFS")

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    try:
        print("Uploading file and updating blockchain...")
        blockchain_hash = add_to_blockchain(filename)
        
    except:
        pass
