import mysql.connector

con = mysql.connector.connect(
    host = '127.0.0.1',
    user = "root",
    password = "Qwer.1234@",
    database = "bankdb"
)
crsr = con.cursor()

def create_account():
    name = input("Enter Your Name: ")
    balance = float(input("Enter Your Balance: "))
    
    query = """
                INSERT INTO ACCOUNTS(NAME,BALANCE) 
                VALUES(%s,%s)
            """
    crsr.execute(query,(name,balance))
    con.commit()   
    print("Account Successfully Created..!") 
    
def deposit():
    ac_no = int(input("Enter Your Account Number: "))
    amount = float(input("Enter Amount: "))
    if amount>0:
        query=  """
                UPDATE ACCOUNTS SET BALANCE = BALANCE + %s 
                WHERE AC_NO = %s
                """
        crsr.execute(query,(amount,ac_no))
        con.commit()
        print("Amount Credited Successfully..!")
    else:
        print("Enter valid amount")
        
def withdraw():
    ac_no = input("Enter Your Account Number: ")
    amount = float(input("Enter Amount: "))
    
    query=  """
                SELECT BALANCE FROM ACCOUNTS WHERE AC_NO = %s 
            """
    crsr.execute(query,(ac_no,))
    result = crsr.fetchone()
    
    if result != None:
        balance = result[0]
        if balance >= amount:
            query1= """
                        UPDATE ACCOUNTS SET BALANCE = BALANCE - %s 
                        WHERE AC_NO = %s 
                    """
            crsr.execute(query1,(amount,ac_no))
            con.commit()
            print("Amount Successfully Debited..!")
        else:
            print("Insufficient Balance")
    else:
        print("Account not Found")
    
def check_balance():
    ac_no = int(input("Enter Your Account Number: "))
    
    query=  """
                SELECT * FROM ACCOUNTS WHERE AC_NO = %s
            """
    crsr.execute(query, (ac_no,))
    result = crsr.fetchone()
    con.commit()
    
    if result != None:
        print('<----------Account Details---------->')
        print("Account Number: ",   result[0])
        print("Customer Name: ",    result[1])
        print("Remaining Balance: ",result[2])
        print("-------------------------------------")
    else:
        print("Account not found")
    
def money_transfer():
    sender = int(input("Enter Sender's account number: "))
    receiver = int(input("Enter Receiver's account number: "))
    amount = float(input("Enter your amount: "))
    
    query = """
                SELECT * FROM ACCOUNTS WHERE AC_NO = %s
            """
    crsr.execute(query,(sender,))
    result = crsr.fetchone()
    try:
        if result != None:
            balance = result[2]
            if balance >= amount:
                query1 ="""
                        UPDATE ACCOUNTS SET BALANCE = 
                        BALANCE - %s WHERE AC_NO = %s
                        """
                crsr.execute(query1,(amount,sender))
                
                query2 = """
                            UPDATE ACCOUNTS SET BALANCE = 
                            BALANCE + %s WHERE AC_NO = %s
                        """
                crsr.execute(query2,(amount,receiver))
                con.commit()
                print("Money Transfer Successfully Completed..!")
            else:
                print("Insufficient Funds")
        else:
            print("Account not found")
    except Exception as e:
        con.rollback()
        print("Transaction Failed")
        print(e)
        
def delete_account():
    ac_no = int(input("Enter Your Account Number: "))
    
    query = """
                DELETE FROM ACCOUNTS WHERE AC_NO = %s
            """
    crsr.execute(query,(ac_no,))
    
    if crsr.rowcount > 0:
        con.commit()
        print("Account Successfully Deleted..!")
    else:
        print("Account not Found")

def view_all_accounts():
    query = """
                SELECT * FROM ACCOUNTS
            """
    crsr.execute(query)
    rows = crsr.fetchall()
    
    print("<---------- ALL ACCOUNT DETAILS --------->")
    for row in rows:
        print("\n1.Account Number: ",row[0])
        print("2.Customer Name: ",row[1])
        print("3.Balance : ",row[2])
        print("------------------------------")
        con.commit()
        
print('<========== BANK MANAGEMENT SYSTEM ==========>')

while True:
    print('\n1. CREATE ACCOUNT')
    print('2. DEPOSIT AMOUNT')
    print('3. WITHDRAW AMOUNT')
    print('4. CHECK BALANCE')
    print('5. MONEY TRANSFER')
    print('6. DELETE ACCOUNT')
    print('7. VIEW ALL ACCOUNTS')
    print('8. EXIT FROM APP')

    choice = int(input('Enter your choice: '))

    match (choice):
        case 1: create_account()
        case 2: deposit()
        case 3: withdraw()
        case 4: check_balance()
        case 5: money_transfer()
        case 6: delete_account()
        case 7: view_all_accounts()
        case 8:
            print('THANK YOU, VISIT AGAIN..!')
            break
        case _: print('Invalid Choice..!')
    