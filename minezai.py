from hashlib import sha256

MAX_NONCE = 100000000

def hash(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = sha256(text.encode('ascii')).hexdigest()
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash
        
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    # for nonce in range(MAX_NONCE):
    #     text = str(block_number) + transactions + previous_hash + str(nonce)
    #     new_hash = sha256(text)
    # return new_hash

transactions = '''
Saikrishna -> Sai -> 100
Sai -> Krishna -> 200
'''
difficulty = 7
new_hash = mine(2,transactions, hash('saikrishna'),difficulty)
print(new_hash)
