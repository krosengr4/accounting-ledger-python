import user_interface, file_manager
from transaction import Transaction

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

def display_deposits():
    print('deposits') 

def display_payments():
    print('payments')

