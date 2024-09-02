# fileChain
A decentralized file sharing system which ensures safety, security and anonimity over the internet.

PreRequisites for this 
  -The pip3 install of the requirements.txt 
  -Create a pinata account and connect the api in the following way
    -go to terminal and type the following command
      touch .env
      nano .env
      (This Opens the in terminal text editor)
      Type PINATA_JWT_TOKEN = '<api key>'  You are set to go ahead

Run the following command
  -python3 temp.py
  -Then go to the following url
    -localhost:5000 / http://localhost:5000 / 127.0.0.1/5000

# fileChain

A decentralized file sharing system which ensures safety, security and anonimity over the internet. Mainly designed to be used by whistleblowers who require more than just anonimity. 

How the application works is basically. It first connects to the pinata api and then uploads a file into the pinata ipfs. After thats done it fetches the CID and loads it into the blockchain and then the complete block hash is calculated. Once it is stored we can find out the CID by the hash value using the function in the localhost site.
