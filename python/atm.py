balance = 5000
pin = 1234

print("Welcome to the ATM!")
entered_pin = int(input("Please enter your PIN: "))

if entered_pin == pin:
    while True:
        print("1. check balance")
        print("2. deposit money")
        print("3. withdrawn money")
        print("4. exit")
        choice = input("selact your choice(1-4):")
        if choice == "1":
            print(f"your corrent balance is:${balance}")
        elif choice == "2":
            amount = float(input("enter amount to deposit:$"))
            if amount >0:
                balance += amount
                print(f"${amount}deposited successfuly.")   
                print(f"new balance:${balance}")
            else:
                print("please enter avalid amount.")
        elif choice == "3":
            amount = float(input("enter amount to deposit:$"))
            if amount <= 0:
                print("please enter a valid amount")
            elif amount > balance:
                print("insufficient balance!")
            else :
                balance -= amount
                print(f"${amount}withdrawn successfully.")
                print(f"remainging balance:${balance}")
        elif choice == "4":
            print("thank you for using the atm.")
            break
        else:
            print("invalid choice!")
    else:
        print("incorrect pin!")        
