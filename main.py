

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_symbols = {"+": add,
                "-": subtract,
                "*": multiply,
                "/": divide
}


def calc_start():
    num1 = int(input("What is the first number?: "))

    for symbol in math_symbols:
        print(symbol)

    user_symbol = input("Pick an operation from the above: ")
    num2 = int(input("What is the second number?: "))
    operation = math_symbols[user_symbol]
    result = operation(num1, num2)


    print(f"{num1} {user_symbol} {num2} = {result}")

    return result

memory_num = calc_start()

while True:
    play_again = input("Would you like to add another operation or start new? 'Y' or 'N'").lower()
    if play_again == "y":
        for symbol in math_symbols:
            print(symbol)
        user_symbol = input("Pick another operation: ")
        num3 = int(input("What is the next number?: "))
        operation = math_symbols[user_symbol]
        answer = operation(memory_num, num3)

        print(f"{memory_num} {user_symbol} {num3} = {answer}")
        memory_num = answer
    elif play_again == "n":
        memory_num = 0
        calc_start()