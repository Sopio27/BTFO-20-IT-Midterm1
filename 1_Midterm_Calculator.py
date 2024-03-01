#List of available operators for calculations
operatorsList = ["+", "-", "*", "/"]

#Calculation class for operations
class Calculations():
    
    #initializes two objects passed by the user
    def __init__(self, firstValue, secondValue):
        #first object passed by the user
        self.firstValue = firstValue
        #second object passed by the user
        self.secondValue = secondValue

    #define operations and retrieve operation chosen by the user
    def operation(self, operation):

        #addition
        if operation == '+':
            return self.firstValue + self.secondValue
        #subtraction
        elif operation == '-':
            return self.firstValue - self.secondValue
        #multiplication
        elif operation == '*':
            return self.firstValue * self.secondValue
        #division
        elif operation == '/':
            return self.firstValue / self.secondValue

#data type validation for values
def checkDataType(value):
    #if passed value is not numeric return error message until the value is the correct type (float)
    while True:
        try:
            userValue = float(value)  
            return userValue
        except ValueError:
            value = checkDataType(input("Incorrect data type. Please, enter a number:  "))

    #cast string value to float
    # return float(value)


print(f"List of available operators {operatorsList}")
#first value passed by the user
x = input("Enter first number: ")
#check and cast the correct result to float
x = checkDataType(x)

#second value passed by the user
y = input("Enter second number: ")
#check and cast the correct result to float
y = checkDataType(y)

#user chooses the operation by inputting an operator
operator = input("Enter an operator: ")

#if the chosen operation is unavailable, return error message until the user chooses available operator
while operator not in operatorsList:
    print(f"List of available operators {operatorsList}")
    operator = input("Such operator is unavailable. Please, try another one: ")  

#initialize calculations class
calculations = Calculations(x,y)

#save result
output = calculations.operation(operator)

#print result
print(f"result: {output}")