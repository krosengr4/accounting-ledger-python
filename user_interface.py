
def display_main_menu():
    print('\n\t-----MAIN MENU------')
    print("""
            ---OPTIONS---
        1 - Add a deposit
        2 - Add a payment
        3 - Go to Ledger Screen
        4 - Go to Reports Screen
              
        0 - Exit application
        """)
        
    return int(input('Enter option:\n'))

def display_ledger_screen():
    print('\n\t-----LEDGER SCREEN-----')
    print("""
            ---OPTIONS---
          1 - Display all entries
          2 - Display deposits
          3 - Display payments
        
          0 - Go back
        """)
    
    return int(input('Enter option:\n'))

def display_reports_screen():
    print('\n\t-----REPORTS SCREEN-----')
    print("""
            ---OPTIONS---
          1 - View all transactions this month
          2 - View all transactions last month
          3 - View all transactions this year
          4 - View all transactions last year
          5 - Search by vendor

          0 - Go back
          """)
    
    return int(input('Enter option:\n'))
    
