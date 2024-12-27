print("Hello user")
balance = 1000.00

user_pin = 1234
PIN = int(input("Enter your PIN: "))
atm_on = False

if PIN == user_pin:
    atm_on = True

else:
    atm_on = False

while atm_on:
    print("***Menu***")
    print("1 - check balance")
    print("2 - deposit money")
    print("3 - withdraw money")
    print("4 - exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYour account balance is: ", balance, "\n")

    elif choice == "2":
        deposit_amount = float(input("Enter your deposit amount: "))
        balance = balance + deposit_amount
        print("\nBalance after deposit is: ", balance, "\n")

    elif choice == "3":
        withdraw_amount = float(input("Enter your withdraw amount: "))
        if withdraw_amount > balance:
            print("\nBalance insufficient\n")
        else:
            balance = balance - withdraw_amount
            print("\nBalance after withdraw is: ", balance, "\n")

    elif choice == "4":
        print("\nThank you\n")
        exit(0)

    else:
        print("\nInvalid choice. Try again\n")
