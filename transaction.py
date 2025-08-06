class Transaction:

    def __init__(self, date, time, description, vendor, amount):
        self.date = date
        self.time = time
        self.description = description
        self.vendor = vendor
        self.amount = amount
    
    def print_data(self):
        print('Date:', self.date)
        print('Time:', self.time)
        print('Description:', self.description)
        print('Vendor:', self.vendor)
        print(f'Amount: ${self.amount:,.2f}')