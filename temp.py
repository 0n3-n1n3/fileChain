from flask import Flask, request, render_template
import os
import json
from upload import add_to_blockchain
from retrieve_cid import get_cid_from_blockchain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        filename = file.filename
        file.save(filename)
        try:
            blockchain_hash = add_to_blockchain(filename)
            os.remove(filename)  # Clean up file after processing
            return render_template('result.html', blockchain_hash=blockchain_hash)
        except Exception as e:
            return render_template('result.html', blockchain_hash=f"An error occurred: {e}")
    else:
        return "No file uploaded."

@app.route('/retrieve_cid', methods=['POST'])
def retrieve_cid():
    hash_value = request.form.get('hash')
    if not hash_value:
        return render_template('cid_results.html', cid="Hash value is required.")
    
    cid = get_cid_from_blockchain(hash_value)
    return render_template('cid_results.html', cid=cid)

@app.route('/update_blockchain')
def update_blockchain():
    # This endpoint can be used to update the blockchain, similar to upload
    return render_template('update_result.html', blockchain_hash="Manual update not supported via this route.")

if __name__ == "__main__":
    app.run(debug=True)

