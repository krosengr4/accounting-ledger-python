import user_interface, file_manager
from transaction import Transaction

# Process user selection from ledger screen menu
def process_ledger_screen():
    if_continue = True

    while(if_continue):
        user_choice = user_interface.display_ledger_screen()

        match user_choice:
            case 1: 
                display_all()
            case 2:
                display_deposits()
            case 3:
                display_payments()
            case 0:
                if_continue = False
            case _:
                print("Please enter a valid option!!!")

# Read and display all transactions in file
def display_all():
    transactions = file_manager.read_file()
    for line in transactions:
        if 'DATE' in line:
            continue
        
        line_parts = line.split('|')

        date = line_parts[0]
        time = line_parts[1]
        description = line_parts[2]
        vendor = line_parts[3]
        amount = float(line_parts[4])

        new_transaction = Transaction(date, time, description, vendor, amount)
        new_transaction.print_data()
        
    input('Press enter to continue')

# Read and display only deposit transactions(positive amount)
def display_deposits():
    transactions = file_manager.read_file()

    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        amount = float(line_parts[4])

        if amount > 0:
            new_transaction = Transaction(line_parts[0], line_parts[1], line_parts[2], line_parts[3], amount)
            new_transaction.print_data();

    input('\nPress enter to continue...')


# Read and display all payment transactions(negative amount)
def display_payments():
    transactions = file_manager.read_file()

    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        amount = float(line_parts[4])

        if amount < 0:
            new_transaction = Transaction(line_parts[0], line_parts[1], line_parts[2], line_parts[3], amount)
            new_transaction.print_data();

    input('Press enter to continue...')


# def display_data(transaction):