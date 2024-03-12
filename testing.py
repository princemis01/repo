import shelve

def display_menu():
    print("Calculator")
    print("==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")
    print()

def get_valid_input():
    while True:
        try:
            num = int(input("Enter your choice (1-6): "))
            if 1 <= num <= 6:
                return num
            else:
                print("Invalid input. Please enter a number between 1 and 6")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6")

def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"Result: {num1:.2f} + {num2:.2f} = {result:.2f}")
    return result

def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"Result: {num1:.2f} - {num2:.2f} = {result:.2f}")
    return result

def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"Result: {num1:.2f} * {num2:.2f} = {result:.2f}")
    return result

def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        return None
    else:
        result = num1 / num2
        print(f"Result: {num1:.2f} / {num2:.2f} = {result:.2f}")
        return result

def show_history():
    with shelve.open('history.db') as db:
        if 'history' not in db:
            print("No history available")
        else:
            history = db['history']
            for item in history:
                print(item)

def main():
    display_menu()
    while True:
        choice = get_valid_input()
        if choice == 1:
            add()
        elif choice == 2:
            subtract()
        elif choice == 3:
            multiply()
        elif choice == 4:
            divide()
        elif choice == 5:
            show_history()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6")
        print()

if __name__ == "__main__":
    main()