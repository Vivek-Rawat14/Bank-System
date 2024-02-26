import mysql.connector as connections
import time

con = connections.connect(host="localhost", username="root", database="bank")
cursor = con.cursor()


def check(pan, addar, phone):
    cursor.execute(
        f'select * from banksystem where pan={pan} and adhar ={addar} and phone={phone}')
    data = cursor.fetchall()
    if len(data) > 0:
        return True


def createaccount():
    print("{:>52}".format("----->Create Your Bank Account<-----"))
    name = input("Enter Your Full Name: ").upper()
    fname = input("Enter Your Father Name: ").upper()
    mname = input("Enter Your Mother Name: ").upper()
    email = input("Enter Your E-mail: ").upper()
    phone = (input("Enter Your Phone Number: "))
    if len(phone) != 10:
        print("Please Enter Proper Phone Number")
        time.sleep(1)
        createaccount()
    address = input("Enter Your Address: ").upper()
    age = int(input("Enter Your Age: "))
    if age < 18:
        print("You are not eligible for opening account")
        time.sleep(1)
        createaccount()
    gender = input("Enter Your Gender: ").upper()
    pan = input("Enter Your Pan Card Number: ").upper()
    if len(pan) != 10:
        print("Please Enter Proper Pan Card Number: ")
        time.sleep(1)
        createaccount()
    adharcard = input("Enter Your Adhar Card Number: ").upper()
    if len(adharcard) != 12:
        print("Please Enter Proper Adhar Card Number: ")
        time.sleep(1)
        createaccount()
    epassword = input("Please Enter 6 Digit Password (While login): ")
    if len(epassword) != 6:
        print("Please Enter 6 digit password")
        time.sleep(1)
        createaccount()

        if check(pan, adharcard, phone):
            print(
                "This Pan Card Number,Adhar Card number or phone number is already exists")
            time.sleep(1)
            createaccount()

    cursor.execute(f'''insert into banksystem(name,father_name,mother_name,age,gender,phone,
                           pan,adhar,email,lpass,address) values("{name}","{fname}","{mname}",{age},
                           "{gender}",{phone},"{pan}","{adharcard}","{email}",{epassword},"{address}"   )''')

    con.commit()
    print("Your Account is Successfully created")
    id = cursor.execute("")
    input("Enter any key to quit: ")
    login()


useraccount = ""


def loginacc():
    global useraccount
    print("{:>55}".format("----->Login<-----"))
    userid = int(input("Enter Your ID: "))
    print("If you forget the password please type 'f' ")
    passw = input("Enter 6 digit Password: ")
    if (passw.lower() == 'f'):
        cursor.execute(f'select email from banksystem where id={userid}')
        res = cursor.fetchall()
        if (len(res) >= 1):
            forget()
            pass
        else:
            print("No account Found")
        pass
    else:
        cursor.execute(
            f'select * from banksystem where id={userid} and lpass = {passw} ')
        res = cursor.fetchall()
        if (len(res) >= 1):
            useraccount = userid
            print("Successfully login")
            time.sleep(1)
            print("")
            category()
        else:
            print("Invalid Credentials")
            login()


def forget():

    phone = input("Enter Your Phone Number: ")
    if len(phone) != 10:
        print("Please Enter Proper Phone Number: ")
        forget()
    npas = input("Enter 6 digit New Password: ")

    if len(npas) == 6:
        print("Wait For Changes")
        cursor.execute(f'''update banksystem set lpass = {npas}  where phone = {phone} ''')
        con.commit()
        time.sleep(2)
        print("Your Password As Been Change")
        input("Enter any key to quit: ")
        loginacc()
    else:
        print("please Enter Proper Password")
        forget()


def category():
    print("{:>55}".format("----->Welcome To Our Bank<-----"))
    print("1.Update Account          2.Create Pin")
    print("3.Withdraw Amount         4.Deposit Amount")
    print("5.Balance Check           6.Quit")
    print("{:>55}".format("----->Choice 1/2/3/4/5/6<-----"))
    print("")
    user = int(input("Enter: "))
    if user == 1:
        updateacc()
    elif user == 2:
        createpin()
    elif user == 3:
        withdraw()
    elif user == 4:
        deposit()
    elif user == 5:
        balance()
    elif user == 6:
        login()


def updateacc():
    print("{:>55}".format("----->Update Account<-----"))
    id = int(input("Enter your id: "))
    p = int(input("Enter Your Phone Number: "))
    if p != 10:
        print("Please Enter Proper Phone Number")
        updateacc()
    name = input("Enter Your Full Name: ").upper()
    fname = input("Enter Your Father Name: ").upper()
    mname = input("Enter Your Mother Name: ").upper()
    email = input("Enter Your E-mail: ").upper()
    phone = (input("Enter Your Phone Number: "))
    if len(phone) != 10:
        print("Please Enter Proper Phone Number")
        time.sleep(1)
        createaccount()
    address = input("Enter Your Address: ").upper()
    age = int(input("Enter Your Age: "))
    if age < 18:
        print("You are not eligible for opening account")
        time.sleep(1)
        createaccount()
    gender = input("Enter Your Gender: ").upper()
    pan = input("Enter Your Pan Card Number: ").upper()
    if len(pan) != 10:
        print("Please Enter Proper Pan Card Number: ")
        time.sleep(1)
        createaccount()
    adharcard = input("Enter Your Adhar Card Number: ").upper()
    if len(adharcard) != 12:
        print("Please Enter Proper Adhar Card Number: ")
        time.sleep(1)
        createaccount()

    cursor.execute(
        f'''update banksystem set name = "{name}",father_name = "{fname}",mother_name="{mname}",
             email = "{email}",age={age},address="{address}",gender = "{gender}",pan="{pan}",
                adhar ="{adharcard}" where id = {id} ''')
    con.commit()
    print("Your Account as been updated")
    input("Enter any key to quit: ")
    category()

def createpin():
    phone = input("Enter Your Phone Number: ")
    if phone != 10:
        print("Please Enter Proper Phone Number: ")
    id = ("Enter Your ID: ")
    mainpass = input("Enter 4 digit Password: ")
    if len(mainpass) != 4:
        print("Enter 4 Digit Password")
        createpin()        
    cursor.execute(
        f'''Update banksystem set("{mainpass}") where id={id} and phone = {phone}''')
    con.commit()
    print("Your pin is created")
    input("Enter any key to quit: ")
    category()

def deposit():
    global useraccount
    pas = input("Enter the pin: ")
    amount = input("Enter the Deposit Amount: ")
    cursor.execute(f''' select * from banksystem  where id = {useraccount} and pin = {pas}''')
    res=cursor.fetchall()
    if len(res) >= 1 :
        cursor.execute(f'''update banksystem set amount  = amount + {amount} where id = {useraccount}    ''')
        con.commit()
        print("Your money is successfully deposit to your account")
        input("Enter any key to quit: ")
        category()
    else :
        print('Invalid PIN')
        deposit()

def withdraw():
    global useraccount
    pas = input("Enter the pin: ")
    wd = input("Enter the Amount: ")
    cursor.execute(f''' select * from banksystem  where id = {useraccount} and pin = {pas}''')
    res=cursor.fetchall()
    if len(res) >= 1 :
        cursor.execute(f'''update banksystem set amount  = amount - {wd} where id = {useraccount}    ''')
        con.commit()
        print(f"You withdraw amount of {wd}")
        input("Enter any key to quit: ")
    else :
        print('Invalid PIN')
        withdraw()
    

def balance():
    pas = input("Enter the pin: ")
    print("{:>55}".format("----->Total Balance Remaining<-----"))
    cursor.execute(f''' select amount from banksystem where pin={pas}''')
    data = cursor.fetchall()
    for i in data:
        print(f"Your balance is {i[0]}")
        input("Enter any key to quit: ")
    category()

def login():
    print("{:>55}".format("----->Welcome To Our Bank<-----"))
    time.sleep(2)
    print("If you want to login account type 'l'")
    print("If you want to Create account type 'c' ")

    user = input("Enter :  ").lower()
    if user == 'l':
        loginacc()
    elif user == 'c':
        createaccount()


login()
