from transaction import Transaction

file_path = 'resources/transactions.txt'

def write_to_file(transaction):
    date = transaction.date
    time = transaction.time
    description = transaction.description
    vendor = transaction.vendor
    amount = transaction.amount

    try:
        with open(file_path, 'a') as file:
            file.write('\n' + date + '|' + time + '|' + description + '|' + vendor + '|' + amount)

        print("The transaction was logged to the file!!!")
    
    except FileNotFoundError as err:
        print("The file was not found! :( )")
    
