from datetime import datetime
from hashlib import sha256

# print(datetime.now())

class Block: 
    def __init__(self, transactions, previous_hash, nonce = 0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_block(self):
        print(f'timestamp: {self.timestamp}')
        print(f'transactions: {self.transactions}')
        print(f'current_hash: {self.generate_hash()}')


    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())

        return block_hash.hexdigest()

    def print_contents(self):
        print(f'timestamp: {self.timestamp}')
        print(f'transactions: {self.transactions}')
        print(f'current_hash: {self.generate_hash()}')
        print(f'previous_hash: {self.previous_hash}')



# block_one = Block(300, 0000)

# Block.print_block(block_one)




# text = 'i am Dio'
# hash_result = sha256(text.encode())

# # print(hash_result.hexdigest())