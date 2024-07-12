from cardHolder import CardHolder

def print_menu():
    # Print options to the user
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(current_user):
    try:
        deposit_amount = float(input("How much money do you want to deposit? "))
        current_user.set_balance(current_user.get_balance() + deposit_amount)
        print("Thank you for your deposit. Your new balance is:", current_user.get_balance())
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def withdraw(current_user):
    try:
        withdraw_amount = float(input("How much money would you like to withdraw? "))
        if current_user.get_balance() < withdraw_amount:
            print("Insufficient balance. Please try again.")
        else:
            current_user.set_balance(current_user.get_balance() - withdraw_amount)
            print("Withdrawal successful. Your new balance is:", current_user.get_balance())
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def check_balance(current_user):
    print("Your current balance is:", current_user.get_balance())

if __name__ == "__main__":
    # Create a list of card holders
    list_of_cardHolders = [
        CardHolder("3490693153147110", 1432, "John", "Dale", 150.33),
        CardHolder("3244514677898555", 3623, "Ashley", "Vincenza", 843.52),
        CardHolder("1226702065767566", 9089, "Matt", "Nugent", 487.67),
        CardHolder("9359806484094961", 7642, "Veronica", "Tapaldo", 654.22),
        CardHolder("2845436543254334", 5434, "Jay", "Williams", 752.99),
        CardHolder("5364654546466551", 2244, "Sarah", "Beaufort", 216.77)
    ]

    # Prompt user for debit card number
    current_user = None
    while True:
        debitCardNum = input("Please insert your debit card number: ")
        debitMatch = [holder for holder in list_of_cardHolders if holder.get_cardNum() == debitCardNum]
        if debitMatch:
            current_user = debitMatch[0]
            break
        else:
            print("The card number you entered is not recognized. Please try again.")

    # Prompt user for PIN
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if current_user.get_pin() == userPin:
                break
            else:
                print("Invalid PIN. Please try again.")
        except ValueError:
            print("Invalid PIN format. Please enter a numeric PIN.")

    # Print options
    print("Welcome", current_user.get_firstName())
    option = 0

    while option != 4:
        print_menu()
        try:
            option = int(input())

            if option == 1:
                deposit(current_user)
            elif option == 2:
                withdraw(current_user)
            elif option == 3:
                check_balance(current_user)
            elif option == 4:
                break
            else:
                print("Invalid input. Please enter a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Thank you! Have a nice day.")
