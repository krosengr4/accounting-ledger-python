try:
    import main_logic
    print("Import successful")
    print("Available functions:", dir(main_logic))
except Exception as e:
    print(f"Import error: {e}")

def main():
    print('\n----------WELCOME TO THE ACCOUNTING LEDGER!----------')
    main_logic.process_home_screen()

    print('\nGoodbye!!!')

main()