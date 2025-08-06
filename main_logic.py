import user_interface, ledger_logic, reports_logic, file_manager
from datetime import datetime
from transaction import Transaction

def process_home_screen():
    if_continue = True

    while(if_continue):
        user_choice = user_interface.display_main_menu()

        match user_choice:
            case 1:
                add_deposit()
            case 2:
                add_payment()
            case 3:
                ledger_logic.process_ledger_screen()
            case 4:
                reports_logic.process_reports_screen()
            case 0:
                if_continue = False
                break
            case _:
                print('Enter a number that is listed in the menu!!!')



def add_deposit():
    trans_date = datetime.now().date()
    trans_time = datetime.now().time()
    description = input('\nEnter the description:\n')
    vendor = input('Enter the vendor:\n')
    amount = float(input('Enter the amount:\n'))

    new_transaction = Transaction(trans_date, trans_time, description, vendor, amount)
    file_manager.write_to_file(new_transaction)
    print('___________________________________________________')
    new_transaction.print_data()


def add_payment():
    trans_date = datetime.now().date()
    trans_time = datetime.now().time()
    description = input('\nEnter the description:\n')
    vendor = input('Enter the vendor:\n')
    amount = float(input('Enter the amount:\n'))

    amount = -amount

    new_transaction = Transaction(trans_date, trans_time, description, vendor, amount)
    file_manager.write_to_file(new_transaction)
    print('___________________________________________________')
    new_transaction.print_data()
