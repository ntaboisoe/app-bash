def calc():
    input_1 = int(input('Enter the first number (integer)'))
    input_2 = int(input('Enter the second number (integer)'))
    operation = input('Enter the type of operation e.g. +, -, /, * ')
    result = None
    
    if type(input_1) == int and type(input_2) == int and type(operation) == str:
        if operation == '+':
            result =  input_1 + input_2
        elif operation == '-':
            result = input_1 - input_2
        elif operation == '*':
            result = input_1 * input_2
        elif operation == '/':
            result = input_1 / input_2
        else:
            return 'Error'
    print(f"The result of your computation is {result}.")


calc()
