import user_interface, file_manager
from transaction import Transaction

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
    print('Transactions this month')

def trans_last_month():
    print('Transactions last month')

def trans_this_year():
    print('Transactions this year')

def trans_last_year():
    print('Transactions last year')