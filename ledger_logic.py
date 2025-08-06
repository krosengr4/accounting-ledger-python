import user_interface, file_manager

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
    print('display all')  

def display_deposits():
    print('deposits') 

def display_payments():
    print('payments')

