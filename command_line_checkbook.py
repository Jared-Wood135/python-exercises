# =======================================================================================================
# TABLE OF CONTENTS START
# =======================================================================================================

#       PLANNING
#       FUNCTIONS
#           - MENU
#           - TIME
#           - DATE
#           - CURRENT BALANCE
#           - WITHDRAWL
#           - DEPOSIT
#           - HISTORY
#           - CLEAR TERMINAL
#       END PRODUCT

# =======================================================================================================
# TABLE OF CONTENTS END
# TABLE OF CONTENTS TO PLANNING
# PLANNING START
# =======================================================================================================

# If statements (Notify if invalid input)
#       - View current balance
#           - Display current balance
#       - Add A Debit(Withdrawl)
#           - Ask for input
#           - Add id, time, amount to csv
#       - Add A Credit(Deposit)
#           - Ask for input
#           - Add id, time, amount to csv
#       - Exit
#           - break function
#       EXTRA:
#           -   X   HISTORICAL TRANSACTIONS
#           -   X   CATEGORY PER TRANSACTION
#           -   X   SUMMARY BY CATEGORY
#           -   X   DATE-TIME
#           -       TRANSACTION BY DAY
#           -       OPTIONAL DESCRIPTION INPUT
#           -       TRANSACTIONS BY DESCRIPTION INPUT
#           -       OPTIONAL PAST MODIFICATION

# =======================================================================================================
# PLANNING END
# PLANNING TO FUNCTIONS
# FUNCTIONS START
# =======================================================================================================

# ====================> MENU FUNCTION <====================
def menu():
    '''
    Main Menu for checkbook
    '''
    # vvv BODY/OUTPUT vvv
    clear()
    while True:
        print(
              "==>  MAIN MENU <==\n\n"
              "(1) View Current Balance\n"
              "(2) Add A Debit (Withdrawl)\n"
              "(3) Add A Credit (Deposit)\n"
              "(4) History of Transactions\n"
              "(5) Exit Program\n"
             )
        menuin = input("Hello!  What would you like to do?\n")
        if menuin == '1':
            clear()
            balance()
        elif menuin == '2':
            clear()
            withdrawl()
        elif menuin == '3':
            clear()
            deposit()
        elif menuin == '4':
            clear()
            history()
        elif menuin == '5':
            clear()
            print("Goodbye!")
            break
        else:
            clear()
            print("Invalid input")

# ====================> TIME FUNCTION <====================
def time():
    '''
    Gets current time in HH:MM:SS
    '''
    # vvv IMPORTS vvv
    import datetime
    # vvv VARIABLES vvv
    current_time = datetime.datetime.now().time()
    time_str = current_time.strftime("%H:%M:%S")
    # vvv OUTPUT vvv
    return(time_str)

# ====================> DATE FUNCTION <====================
def date():
    '''
    Gets current date DD-MMM-YYYY
    '''
    # vvv IMPORTS vvv
    import datetime
    # vvv VARIABLES vvv
    current_date = datetime.datetime.now()
    date_str = current_date.strftime("%d-%b-%Y")
    # vvv OUTPUT vvv
    return(date_str)

# ====================> CURRENT BALANCE FUNCTION <====================
def balance():
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv GET TOTAL DEPOSITS vvv
    with open('command_line_checkbook_transactions.csv', 'r') as read:
        reader = csv.DictReader(read)
        next(reader)
        alldeposits = ([float(row['amount']) for row in reader if 'deposit' in row['category']])
        totaldeposits = sum(alldeposits)
    # vvv GET TOTAL WITHDRAWLS vvv
    with open('command_line_checkbook_transactions.csv', 'r') as read:
        reader = csv.DictReader(read)
        next(reader)
        allwithdrawls = ([float(row['amount']) for row in reader if 'withdrawl' in row['category']])
        totalwithdrawls = sum(allwithdrawls)
    # vvv CURRENT BALANCE vvv
    print(f"${totaldeposits - totalwithdrawls} as of {date()} // {time()}")
    print("")

# ====================> WITHDRAW FUNCTION <====================
def withdrawl():
    '''
    All withdrawls from 'command_line_checkbook_transactions.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv INITIAL MENU vvv
    print(
          "==> WITHDRAWL MENU <==\n\n"
          "(1) Make A Withdrawl\n"
          "(2) Summary of Withdrawls\n"
          "(3) Back To Main Menu\n"
         )
    menuin = input("Welcome to the 'Withdrawl Menu'!  What would you like to do?\n")
    while True:
        # vvv MAKE A WITHDRAW vvv
        if menuin == '1':
            clear()
            # vvv VARIABLES vvv
            withdrawin = input('How much would you like to withdraw?\n')
            cols = ['id', 'date', 'time', 'category', 'amount', 'description']    
            # vvv IF CSV FILE DOESN'T EXIST...  CREATE FILE vvv
            if os.path.exists('command_line_checkbook_transactions.csv') == False:
                print("Creating 'command_line_checkbook_transactions.csv' file...")
                with open('command_line_checkbook_transactions.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writeheader()
                    writer.writerow(
                        {
                            'id' : 0,
                            'date' : date(),
                            'time' : time(),
                            'category' : '',
                            'amount' : 0,
                            'description' : ''
                        }
                    )
                if os.path.exists('command_line_checkbook_transactions.csv') == True:
                    print("Successfully created file...\nReturning to 'Main Menu'")
                    print("")
                    break
                else:
                    print("Failed to create file...\nReturning to 'Main Menu'")
                    print("")
                    break
            # vvv IF CSV FILE EXIST... EDIT FILE vvv
            elif os.path.exists('command_line_checkbook_transactions.csv'):
                # vvv MAX ID VALUE FROM CSV
                with open('command_line_checkbook_transactions.csv', 'r') as read:
                    reader = csv.reader(read)
                    next(reader)
                    max_id = max([int(row[0]) for row in reader])
                    new_id = max_id + 1
                # vvv CREATE NEW LINE vvv
                with open('command_line_checkbook_transactions.csv', 'a') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writerow(
                        {
                            'id' : new_id,
                            'date' : date(),
                            'time' : time(),
                            'category' : 'withdrawl',
                            'amount' : withdrawin,
                            'description' : 'description'
                        }
                    )
                clear()
                print(f"${withdrawin} logged on {time()}...\nReturning to 'Main Menu'")
                print("")
                break
        # vvv IF USER WANTS SUMMARY OF WITHDRAWLS vvv
        elif menuin == '2':
            with open('command_line_checkbook_transactions.csv', 'r') as f:
                reader = csv.DictReader(f)
                next(reader)
                allwithdrawls = ([float(row['amount']) for row in reader if 'withdrawl' in row['category']])
                sumwithdrawls = sum(allwithdrawls)
                clear()
                print(f"Total Withdrawls ==> ${sumwithdrawls}")
                print("")
                break
        # vvv IF USER INPUT WANTS TO GO BACK TO MAIN MENU vvv    
        elif menuin == '3':
            clear()
            print("Returning to 'Main Menu'...")
            print("")
            break
        # vvv IF INPUT IS INVALID vvv
        else:
            clear()
            print("Invalid input...\nReturning to 'Main Menu'")
            print("")
            break
    
# ====================> DEPOSIT FUNCTION <====================
def deposit():
    '''
    All deposits from 'command_line_checkbook_transactions.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv INITIAL MENU vvv
    print(
          "==> DEPOSIT MENU <==\n\n"
          "(1) Make A Deposit\n"
          "(2) Summary of Deposits\n"
          "(3) Back To Main Menu\n"
         )
    menuin = input("Welcome to the 'Deposit Menu'!  What would you like to do?\n")
    while True:
        # vvv MAKE A DEPOSIT vvv
        if menuin == '1':
            clear()
            # vvv VARIABLES vvv
            depositin = input('How much would you like to deposit?\n')
            cols = ['id', 'date', 'time', 'category', 'amount', 'description']    
            # vvv IF CSV FILE DOESN'T EXIST...  CREATE FILE vvv
            if os.path.exists('command_line_checkbook_transactions.csv') == False:
                print("Creating 'command_line_checkbook_transactions.csv' file...")
                with open('command_line_checkbook_transactions.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writeheader()
                    writer.writerow(
                        {
                            'id' : 0,
                            'date' : date(),
                            'time' : time(),
                            'category' : '',
                            'amount' : 0,
                            'description' : ''
                        }
                    )
                if os.path.exists('command_line_checkbook_transactions.csv') == True:
                    print("Successfully created file...\nReturning to 'Main Menu'")
                    print("")
                    break
                else:
                    print("Failed to create file...\nReturning to 'Main Menu'")
                    print("")
                    break
            # vvv IF CSV FILE EXIST... EDIT FILE vvv
            elif os.path.exists('command_line_checkbook_transactions.csv'):
                # vvv MAX ID VALUE FROM CSV
                with open('command_line_checkbook_transactions.csv', 'r') as read:
                    reader = csv.reader(read)
                    next(reader)
                    max_id = max([int(row[0]) for row in reader])
                    new_id = max_id + 1
                # vvv CREATE NEW LINE vvv
                with open('command_line_checkbook_transactions.csv', 'a') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writerow(
                        {
                            'id' : new_id,
                            'date' : date(),
                            'time' : time(),
                            'category' : 'deposit',
                            'amount' : depositin,
                            'description' : 'description'
                        }
                    )
                clear()
                print(f"${depositin} logged on {time()}...\nReturning to 'Main Menu'")
                print("")
                break
        # vvv IF USER WANTS SUMMARY OF DEPOSITS vvv
        elif menuin == '2':
            with open('command_line_checkbook_transactions.csv', 'r') as f:
                reader = csv.DictReader(f)
                next(reader)
                alldeposits = ([float(row['amount']) for row in reader if 'deposit' in row['category']])
                sumdeposits = sum(alldeposits)
                clear()
                print(f"Total Deposits ==> ${sumdeposits}")
                print("")
                break
        # vvv IF USER INPUT WANTS TO GO BACK TO MAIN MENU vvv    
        elif menuin == '3':
            clear()
            print("Returning to 'Main Menu'...")
            print("")
            break
        # vvv IF INPUT IS INVALID vvv
        else:
            clear()
            print("Invalid input...\nReturning to 'Main Menu'\n")
            print("")
            break

# ====================> TRANSACTION HISTORY FUNCTION <====================
def history():
    '''
    Gets the history of all transactions
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv BODY/OUTPUT vvv
    with open('command_line_checkbook_transactions.csv', 'r') as f:
        rows = f.readlines()
        headers = rows[0].strip().split(',')
        print(f"{headers[0] : ^25} | {headers[1] : ^25} | {headers[2] : ^25} | {headers[3] : ^25} | {headers[4] : ^25} | {headers[5] : ^25}")
        print(f"{'-------------------------' : ^25} | {'-------------------------' : ^25} | {'-------------------------' : ^25} | {'-------------------------' : ^25} | {'-------------------------' : ^25} | {'-------------------------' : ^25}")
        for row in rows[2:]:
            data = row.strip().split(',')
            print(f"{data[0] : ^25} | {data[1] : ^25} | {data[2] : ^25} | {data[3] : ^25} | {data[4] : ^25} | {data[5] : ^25}")
        print("")

# ====================> CLEAR TERMINAL FUNCTION <====================
def clear():
    '''
    Clears terminal
    '''
    # vvv IMPORTS vvv
    import os
    # vvv BODY/OUTPUT vvv
    os.system('clear')

# =======================================================================================================
# FUNCTIONS END
# FUNCTIONS TO END PRODUCT
# END PRODUCT START
# =======================================================================================================

menu()

# =======================================================================================================
# END PRODUCT END
# =======================================================================================================