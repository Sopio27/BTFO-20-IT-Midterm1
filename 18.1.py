# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს, დაუწერეთ დეკორატორი, რომელიც შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი, თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით, სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან.



def DataValidation(n):
    def decorator(func):
        def wrapper():
            if n > 0:
                func()
            else:
                raise ValueError("The passed value must be a positive number")
        return wrapper
    return decorator

n = int(input("Enter a positive number: "))

@DataValidation(n)
def returnvalues():
    print(n)

returnvalues()