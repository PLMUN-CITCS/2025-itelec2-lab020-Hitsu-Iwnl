def get_integer_input() -> int:
    """Gets and validates an integer input from the user."""
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def check_even_odd(number: int) -> str:
    """Returns whether a number is Even or Odd."""
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."
if __name__ == "__main__":
    """Main program to check if a number is Even or Odd."""
    user_number = get_integer_input()
    print(check_even_odd(user_number))