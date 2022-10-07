import sys

from operations import add, div, mul, sub

print("Welcome the Calculator App")
# Print operations to the console
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Quit")

choice = input("Enter your choice: ")

while choice != "5":
    if choice in ("1", "2", "3", "4"):
        number_1 = float(input("Enter a number: "))
        number_2 = float(input("Enter another number: "))
        if choice == "1":
            add(number_1, number_2)
        elif choice == "2":
            sub(number_1, number_2)
        elif choice == "3":
            mul(number_1, number_2)
        elif choice == "4":
            div(number_1, number_2)
    else:
        print("Invalid Input")
    choice = input("Enter your choice: ")

print("Thank you for using the calculator app. Goodbye.")
sys.exit()
