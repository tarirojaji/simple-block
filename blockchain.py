from typing import ChainMap
from block import Block

class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        # Block([], 0)
        transactions = {}
        genesis_block = Block(transactions, 0)
        self.chain.append(genesis_block)
        return self.chain

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f'Block {i} {current_block}')
            current_block.print_contents()

    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_block_hash)
        self.chain.append(new_block)

blockchain = Blockchain()
t1 = blockchain.add_block(300)

blockchain.print_blocks()