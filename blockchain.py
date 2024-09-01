import hashlib
import json
import os

class Block:
    def __init__(self, cid, phash):
        if cid is None:
            raise ValueError("CID cannot be None")
        self.cid = cid
        self.phash = phash
        self.hash = self.calc()

    def calc(self):
        sha = hashlib.sha256()
        sha.update(self.cid.encode('utf-8'))
        sha.update(self.phash.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.genesis()]
        self.load_data()

    def genesis(self):
        return Block('', '0')

    def new_block(self, cid):
        if cid is None:
            raise ValueError("Cannot add a block with a None CID")
        pblock = self.chain[-1]
        nblock = Block(cid, pblock.hash)
        self.chain.append(nblock)
        self.save_data()
        return nblock.hash

    def save_data(self):
        with open('blockchain_data.json', 'w') as f:
            json.dump({'chain': [block.__dict__ for block in self.chain]}, f, indent=4)

    def load_data(self):
        if os.path.exists('blockchain_data.json'):
            with open('blockchain_data.json', 'r') as f:
                data = json.load(f)
                self.chain = [Block(block['cid'], block['phash']) for block in data['chain']]
        else:
            self.chain = [self.genesis()]

if __name__ == "__main__":
    from sys import argv
    bc = Blockchain()
    if len(argv) > 1:
        cid = argv[1]
        print("New Block Hash:", bc.new_block(cid))

