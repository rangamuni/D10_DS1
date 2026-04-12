balance=1000             #-----Machine Simulation using Python-----#
def deposit():
    amount=int(input("Enter amount: "))
    if amount>0:
        print(f'{amount} is successfully credited..!')
        return amount
    else:
        print("Enter a valid amount greater than zero")
        return 0
def withdrawal():
    amount=int(input("Enter amount: "))
    if amount<=balance:
        print(f'{amount}/- debited successfully..!')
        return amount
    else:
        print("Enter a valid amount less than balance amount")
def check_balance():
    print(f"{balance}/- is your balance ")
print("<---------- WELCOME TO 10K CODERS BANK ----------->")
digital_pin=1289
input_pin=int(input("Enter a pin: "))
chance=3
is_pin=False
for i in range(1,4):
    if input_pin==digital_pin:
        is_pin=True
    else:
        if chance - i !=0:
            print(f'Invalid pin, Enter a valid pin you have only {chance - i} chances left..!')
            input_pin=int(input("Enter a pin: "))
if is_pin:
    while True:
        print("TO ADD MONEY PRESS     -> 1")
        print("TO TAKE MONEY PRESS    -> 2")
        print("TO CHECK MONEY PRESS   -> 3")
        print("TO EXIT FROM APPS PRESS-> 4")
        choice=int(input("Enter a choice: "))
        if choice==1:
            balance+=deposit()
        elif choice==2:
            balance-=withdrawal()
        elif choice==3:
            check_balance()
        elif choice==4:
            print("THANK YOU, VISIT AGAIN")
            break
        else:
            print(f"Invalid choice {choice}, Plz enter a valid options")
else:
    print("Your account has been blocked for 24hrs!!")