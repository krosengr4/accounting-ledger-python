import user_interface, file_manager
from transaction import Transaction
from datetime import datetime

# Process user selection from the report screen menu
def process_reports_screen():
    if_continue = True

    while(if_continue):
        user_choice = user_interface.display_reports_screen()

        match user_choice:
            case 1:
                trans_this_month()
            case 2:
                trans_last_month()
            case 3:
                trans_this_year()
            case 4:
                trans_last_year()
            case 5:
                search_by_vendor()
            case 0:
                if_continue = False
            case _:
                print("Please enter a valid option!!!")           

# Read and print all transactions from this month and year
def trans_this_month():
    print('-----TRANSACTIONS THIS MONTH-----')
    transactions = file_manager.read_file()

    current_month = datetime.now().date().month
    current_year = datetime.now().year

    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        date = line_parts[0]
        time = line_parts[1]
        description = line_parts[2]
        vendor = line_parts[3]
        amount = float(line_parts[4])

        date_parts = date.split('-')
        trans_month = int(date_parts[1])
        trans_year = int(date_parts[0])

        if trans_month == current_month and trans_year == current_year:
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()

    input('\nPlease hit enter to continue...')

# Read and print all transactions from last month
def trans_last_month():
    print('-----TRANSACTIONS LAST MONTH-----')

    transactions = file_manager.read_file()

    current_month = datetime.now().month
    last_month = current_month - 1
    current_year = datetime.now().year
    last_year = current_year - 1

    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        date = line_parts[0]
        time = line_parts[1]
        description = line_parts[2]
        vendor = line_parts[3]
        amount = float(line_parts[4])

        date_parts = date.split('-')
        trans_year = int(date_parts[0])
        trans_month = int(date_parts[1])

        if current_month != 1 and trans_month == last_month and trans_year == current_year:
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()
        elif current_month == 1 and trans_month == 12 and trans_year == last_year:
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()

    input('Press enter to continue')


# Read and print all transactions from this year
def trans_this_year():
    print('-----TRANSACTIONS THIS YEAR-----')
    transactions = file_manager.read_file()

    current_year = datetime.now().year

    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        date = line_parts[0]
        time = line_parts[1]
        description = line_parts[2]
        vendor = line_parts[3]
        amount = float(line_parts[4])

        date_parts = date.split('-')
        trans_year = int(date_parts[0])

        if trans_year == current_year:
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()

    input('\nPlease hit enter to continue...')

# Read and print all transactions from last year
def trans_last_year():
    print('-----TRANSACTIONS LAST YEAR-----')
    transactions = file_manager.read_file()

    last_year = datetime.now().year - 1

    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        date = line_parts[0]
        time = line_parts[1]
        description = line_parts[2]
        vendor = line_parts[3]
        amount = float(line_parts[4])

        date_parts = date.split('-')
        trans_year = int(date_parts[0])

        if trans_year == last_year:
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()

    input('Please hit enter to continue...')

# Read and print all transactions from a vendor user searches
def search_by_vendor():
    transactions = file_manager.read_file()

    user_search = input('\nPlease enter the vendor to search for:\n').lower()
    print('-----TRANSACTIONS FROM', user_search.upper() + '-----')
    
    for line in transactions:
        if 'DATE' in line:
            continue

        line_parts = line.split('|')
        date = line_parts[0]
        time = line_parts[1]
        description = line_parts[2]
        vendor = line_parts[3]
        amount = float(line_parts[4])

        if user_search in vendor.lower():
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()

    input('Press enter to continue...')

        


