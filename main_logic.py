import user_interface, ledger_logic, reports_logic

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
    print('Add a deposit');

def add_payment():
    print('Add payment')
