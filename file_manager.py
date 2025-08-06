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
            file.write('\n' + str(date) + '|' + str(time) + '|' + description + '|' + vendor + '|' + str(amount))

        print("\nThe transaction was logged to the file!!!")
    
    except FileNotFoundError as err:
        print("The file was not found! :( )")

def read_file():
    try:
        with open(file_path) as file:
           result = file.readlines()
           return result

    except FileNotFoundError as err:
        print('The file was not found...') 
    
