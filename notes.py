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

## Working with Inputs

blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction,transaction_amount])

txt_amount = float(input('Your transaction amount please: '))
add_value(txt_amount)

txt_amount = float(input('Your transaction amount please: '))
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=txt_amount)

txt_amount = float(input('Your transaction amount please: '))
add_value(txt_amount, get_last_blockchain_value())

# print(blockchain)