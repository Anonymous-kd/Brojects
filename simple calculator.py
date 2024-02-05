def get_num(): 
  
    while True: 
        try: 
            x = int(input("Enter the num1: ")) 
            y = int(input("Enter the num2: ")) 
            return x, y 
        except ValueError: 
            print("i want numbers bigman") 
 
def get_opp(): 
    
    while True: 
        operator = input("Enter an operator (+, -, *, /): ") 
        if operator in ["+", "-", "*", "/"]: 
            return operator 
        else: 
            print("choose from (+, -, *, /).") 
 
def add(x, y): 
     return x + y 
 
def subtract(x, y): 
    return x - y 
def multiply(x, y): 
     return x * y 
 
def divide(x, y): 
    if y == 0: 
        print("Cant divide by zero. sorry bigman") 
        return None 
    else: 
        return x / y 
 
def exit_program(): 
    print("Exiting the calculator program.") 
    exit() 
 
while True: 
    x, y = get_num() 
    j = get_opp() 
 
    if j == '+': 
        result = add(x, y) 
    elif j == '-': 
        result = subtract(x, y) 
    elif j == '*': 
        result = multiply(x, y) 
    elif j == '/': 
        result = divide(x, y) 
    else: 
        continue 
        print("Invalid operator. Please try again.") 
 
    if result is not None: 
        print(f"The result is: {result}") 
 
    choice = input("Do you want to perform another calculation? (y/n): ") 
    if choice.lower() != 'y': 
        exit_program()