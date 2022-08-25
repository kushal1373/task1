from operator import is_


def add(num1, num2):
    sum = num1+num2
    return(sum)

FNum = int(input("Enter first number"))
SNum = int(input("Enter second number"))
sum = add(FNum, SNum)
print(f"Sum is {sum}")

#2
brand_name = input("Enter brand name:")
model_name = input("Enter Model name:")
price = int(input("Enter price"))

def laptop_specification(brand, model, price):
  print(f"The laptop is {brand}, {model} @ RS.{price}")

mylaptop=laptop_specification(brand_name, model_name, price)
print(mylaptop)



#working of an atm machine

total_price = 0
card_type = "visa"
is_same_bank = True
is_expired = False

def read_card():
    print("Fetching card details from bank...")
    card_details = [1200,False,True]
    total_price = card_details[0]
    is_same_bank = card_details[1]
    is_expired = card_details[2]
    if is_expired:
        print("Sorry this card cant be operated here")
    else:
        perform_transaction(total_price,is_same_bank)

def perform_transaction(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 10
        if required_amt > total_amt:
            return "No enough balance"
        else:
            print(f"Amt withdrawn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")

print("please insert your atm card")
input()
print("card inserted")
required_amt = int(input("Please enter a amt:"))
read_card()




#just a practice

highest_savings = 1000000
lowest_savings = 500
is_same_bank_loan = True
is_not_same_bank = False

def read_status():
    print("fetching the information as follows")
    loan_details = [55000,True,False]
    higest_savings = loan_details[0]
    is_same_bank_loan = loan_details[1]
    is_not_same_bank = loan_details[2]
    if is_not_same_bank:
        print("Sorry your time limit has reached so u cant pay")
    else:
        begin_transactions(highest_savings,is_same_bank_loan)

def begin_transactions(highest_amt, is_same_bank_loan):
    charge = 0
    if not is_same_bank_loan:
        charge = 1000
        if neede_amt > highest_amt:
           return("No Transactions done")
        else:
            print(f"Amt paid: {neede_amt}")
            print(f"Remaining available balance: {highest_amt-neede_amt-charge}")

print("Insert your loan amt to be paid")
input()
print("details entered")
neede_amt= int(input("Please enter a amt:"))
read_status()




