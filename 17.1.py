#ირაკლი, სალამი! ამ დავალების 1 ნაწილი ვერ გავიაზრე კარგად, child მეთოდებს რომ ვიძახებ, როგორ შეიძლება თავდაპირველად
# parent-ში გადაცემულ მნიშვნელობაზე მოქმედება? მაგალითად აქ დეპოზიტს რომ ვუმატებ თანხას 1000-ზე მოქმედებს და არა
#, პირობითად, 240-ზე, რომელიც owner-ით გადავეცი. ალბათ მაგ ინფორმაციის შენაცვა ცალკე იქნება სჭირო, ხომ?

class Person:

    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
        

    def info(self):
        print(f"{self.name}'s deposit balance: {self.deposit}")
        print(f"{self.name}'s credit balance: {self.loan}")

    def offsetDepositAmount(self, name, amount):
        self.deposit = self.deposit + amount
        self.info()

    def offsetLoanAmount(self, name, amount):
        self.loan = self.loan + amount
        self.info()

    def updatePerson(self, person):
        self.name = person

    def __str__(self):
        return f"{self.name} has ${self.deposit} on deposit account and ${self.loan} on credit account"

class House(Person):
    def __init__(self, ID, price, owner, status ="გასაყიდი"):
        self.ID = id
        self.price = price
        self.status = status
        super().__init__(owner)
        self.owner = self.name

    def ownername(self):
        print(f"{self.owner}") 

    def sellHouseTo(self, buyer, amount = None):

        if amount is None:
    
            super().offsetDepositAmount(self.owner, self.price)
            super().updatePerson(buyer)
            self.owner = buyer
            self.status = "გაყიდული"
            print(f"House sold to {self.owner}.")

        else:

            super().offsetDepositAmount(self.owner, self.price)

            self.owner = buyer
            super().updatePerson(buyer)
            super().offsetLoanAmount(self.owner, amount)
            self.status = "გაყიდულია სესხით"
            print(f"House sold to {self.owner} with a mortgage.")


owner = Person("Owen", 240, 10)
buyer = Person("Bob", 2000, 1000)
ownerApartment = House(1, 5000, "Owen")

ownerApartment.sellHouseTo("Bob", 400)
