def check_integer(input_value):
    return input_value.isdigit()

# Example usage
value_to_check = input("Enter a value: ")
if check_integer(value_to_check):
    print("Input is an integer.")
else:
    print("Input is not an integer.")