from blockchain import Blockchain
from hashlib import sha256


t1 = {
    "sender":"Jojo", "receiver": "Dio", "amount":"30"
    }
t2 = {
    "sender": "Dio", "receiver":"Giorgio", "amount":"10"
    }
t3 = {
    "sender":"Speedwagon", "receiver":"Jojo", "amount":"1000"
    }
fake_transaction = {
    "sender":"Jojo", "receiver": "Dio", "amount":"100"
    }


blockchain = Blockchain()
blockchain.add_block(t1)
blockchain.add_block(t2)
blockchain.add_block(t3)
# blockchain.print_blocks()

blockchain.chain[1].transactions = fake_transaction
print(blockchain.chain[1].transactions)
blockchain.validate_chain()

