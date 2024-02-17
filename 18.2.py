# დაწერეთ პირველი დავალება ფუნქტორის გამოყენებით

class DataValidation:

    def __call__(self, x):
    
        if x > 0:
            return x
        else:
             raise ValueError("The passed value must be a positive number")


n = int(input("Enter a positive number: "))

dataValidation = DataValidation()

print(dataValidation(n))