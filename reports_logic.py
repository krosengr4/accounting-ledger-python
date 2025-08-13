import user_interface, file_manager
from transaction import Transaction
from datetime import datetime

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
            case 0:
                if_continue = False
            case _:
                print("Please enter a valid option!!!")           

def trans_this_month():
    transactions = file_manager.read_file()

    current_month = datetime.now().date().month

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

        if trans_month == current_month:
            new_transaction = Transaction(date, time, description, vendor, amount)
            new_transaction.print_data()


def trans_last_month():
    print('Transactions last month')

def trans_this_year():
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

def trans_last_year():
    print('Transactions last year')