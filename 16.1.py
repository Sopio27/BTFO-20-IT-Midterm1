# დავალება 1.

# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount, ისეთი ატრიბუტებით, როგორიცაა account_number, account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები. შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.

class BankAccount:

    def __init__(self,account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def cashIn(self, amount):
        initialBalance = self.balance
        newBalance = initialBalance + amount
        self.balance = newBalance

        print(f"{amount}$ transferred to your account. current balance: {self.balance}")

    def cashOut(self, amount):
        initialBalance = self.balance
        newBalance = initialBalance - amount
        self.balance = newBalance

        print(f"{amount}$ transferred from your account. current balance: {self.balance}")


account = BankAccount(1, "Nick", 10)
account.cashIn(500)
account.cashOut(1)

account2 = BankAccount(2, "Stefan", 0)
account2.cashIn(1000)
account2.cashOut(5)

