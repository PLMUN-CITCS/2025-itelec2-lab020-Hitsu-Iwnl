def get_integer_input():
    """Prompt user for an integer input and return it."""
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    """Return a message indicating if the number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main program
num = get_integer_input()
print(check_even_odd(num))
