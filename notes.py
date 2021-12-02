#### Create a function

blockchain = []

def add_value():
    blockchain.append(5.3)
    #print(blockchain)

add_value()

#### Create a function

blockchain = [[1]]

def add_value(transaction_amount):
    blockchain.append([blockchain[-1],transaction_amount])
    #print(blockchain)

add_value(2)
add_value(0.9)
add_value(10.36)

### create other function

blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(),transaction_amount])

add_value(2)
add_value(0.9)
add_value(10.36)

#print(blockchain)