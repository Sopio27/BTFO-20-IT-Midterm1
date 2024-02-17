# დავალება 3.

# დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი,
# რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი


balance = float(input("Enter current balance: "))
transfer = float(input("Enter amount to transfer: "))

def checkBalance(balance, amount):
    return balance - amount >= 0 

def CommissionFee(b):
    def decorator(func):
        def wrapper(x, y):
            if not checkBalance(b,1):
                print("Not enough money on the account")
            else:
                func(x,y)
        return wrapper
    return decorator


@CommissionFee(balance)
def transaction(x, y):
    x = x - y - 1
    print (f"Transaction has been successfully made. Your leftover balance: {x}")
  

transaction(balance, transfer)
