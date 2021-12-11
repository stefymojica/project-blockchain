blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    user_input = float(input('Your transaction amount please: '))
    return user_input


txt_amount = get_user_input()
add_value(txt_amount)

while True:
    txt_amount = get_user_input()
    add_value(txt_amount, get_last_blockchain_value())

    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

print('Done!')
