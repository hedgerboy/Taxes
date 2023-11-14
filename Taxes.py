import time
import os
import sys


# -----------------  chat GPT ----------------
# Function to clear the terminal screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux (here, os.name is 'posix')
    else:
        _ = os.system('clear')

clear_screen()

# Startup with loading bar
loading_bar_length = 30  # Length of the loading bar
for i in range(loading_bar_length + 1):
    percent = (i / loading_bar_length) * 100
    bar = '#' * i + '-' * (loading_bar_length - i)
    print(f"\rLoading: [{bar}] {percent:.2f}%", end='', flush=True)
    time.sleep(0.1)

print("\nComplete")
time.sleep(1)  # Wait to show the loading complete message

# Display HEDGERCLAN in ASCII art
print("""
  _    _ ______ _____   _____ ______ _____   _____ _               _   _ 
 | |  | |  ____|  __ \ / ____|  ____|  __ \ / ____| |        /\   | \ | |
 | |__| | |__  | |  | | |  __| |__  | |__) | |    | |       /  \  |  \| |
 |  __  |  __| | |  | | | |_ |  __| |  _  /| |    | |      / /\ \ | . ` |
 | |  | | |____| |__| | |__| | |____| | \ \| |____| |____ / ____ \| |\  |
 |_|  |_|______|_____/ \_____|______|_|  \_\ _____|______/_/    \_\_| \_|
                                                                         
                                                                         
 """)

time.sleep(2)  # Wait to show the ASCII art

# Clear the screen
clear_screen()



# Defining input variables
def get_payment_gap():
    while True:
        payment_gap_input = input("When do you get paid? (1 = weekly, 2 = fortnightly, 3 = monthly, Q to quit): ")

        if payment_gap_input.upper() == 'Q':
            print("Exiting the program.")

            time.sleep(1)  # Wait to show the loading complete message
            # Clear the screen
            clear_screen()
            # Display HEDGERCLAN in ASCII art
            print("""
            _    _ ______ _____   _____ ______ _____   _____ _               _   _ 
            | |  | |  ____|  __ \ / ____|  ____|  __ \ / ____| |        /\   | \ | |
            | |__| | |__  | |  | | |  __| |__  | |__) | |    | |       /  \  |  \| |
            |  __  |  __| | |  | | | |_ |  __| |  _  /| |    | |      / /\ \ | . ` |
            | |  | | |____| |__| | |__| | |____| | \ \| |____| |____ / ____ \| |\  |
            |_|  |_|______|_____/ \_____|______|_|  \_\ _____|______/_/    \_\_| \_|
                                                                                    
                                                                                    
            """)

            time.sleep(2)  # Wait to show the ASCII art


            sys.exit(0)  # Exits the program

        if payment_gap_input.isdigit():
            payment_gap = int(payment_gap_input)
            if payment_gap in [1, 2, 3]:
                return payment_gap
            else:
                print("Please enter a valid number (1, 2, or 3).")
        else:
            print("Invalid input. Please enter a number or 'Q' to quit.")

payment_gap = get_payment_gap()

# ^^^^^^^^^^^^ Chat GPT ^^^^^^^^^^^^^^^

income = int(input("Income Per pay(Rounded to nearest dollar): " ))
medicare = input("do you have Private Health insurance? ")
allowable_deductions = int(input("total allowable deductions: "))





# weekly
if payment_gap == 1:
    print(1)
    total_income = (income * 52)

    # creates the taxable income(subttracting the allowable deductions)
    taxable_income = total_income - allowable_deductions

    # will calculate 2% for public health care
    if medicare.lower() != "yes":
        taxable_income = taxable_income * 0.98
    else:
        print("Private Health Insurance")

    print(f"Total taxable income: ${taxable_income}")

        # first tax bracket(no tax)
    if taxable_income <= 18200:
        print("Your total tax is: $0")

    # seccond tax bracket(19% tax rate)
    elif taxable_income <= 45000:
        tax_calculation = ((taxable_income - 18200) * 0.19)
        print(f"Your total tax is: ${tax_calculation}")

    # third tax bracket(32.5% tax rate and $5092 tax)
    elif taxable_income <= 120000:
        tax_calculation1 = (5092 + (taxable_income - 45000) * 0.325)
        print(f"Your total tax is: ${tax_calculation1}")

    # fourth tax bracket(37% tax rate and $29467 tax)
    elif taxable_income <= 180000:
        tax_calculation2 = (29467 + (taxable_income - 120000) * 0.37)
        print(f"Your total tax is: ${tax_calculation2}")

    # fifth tax bracket (45% tax rate and $51667 tax)
    else:
        tax_calculation3 = (51667 + 0.45 * (taxable_income - 180000))
        print(f"Your total tax is: ${tax_calculation3}")

# fortnightly
elif payment_gap == 2:
    print(2)
    total_income = (income * 26)

    # creates the taxable income(subttracting the allowable deductions)
    taxable_income = total_income - allowable_deductions

    # will calculate 2% for public health care
    if medicare.lower() != "yes":
        taxable_income = taxable_income * 0.98
    else:
        print("Private Health Insurance")

    print(f"Total taxable income: ${taxable_income}")

        # first tax bracket(no tax)
    if taxable_income <= 18200:
        print("Your total tax is: $0")

    # seccond tax bracket(19% tax rate)
    elif taxable_income <= 45000:
        tax_calculation = ((taxable_income - 18200) * 0.19)
        print(f"Your total tax is: ${tax_calculation}")

    # third tax bracket(32.5% tax rate and $5092 tax)
    elif taxable_income <= 120000:
        tax_calculation1 = (5092 + (taxable_income - 45000) * 0.325)
        print(f"Your total tax is: ${tax_calculation1}")

    # fourth tax bracket(37% tax rate and $29467 tax)
    elif taxable_income <= 180000:
        tax_calculation2 = (29467 + (taxable_income - 120000) * 0.37)
        print(f"Your total tax is: ${tax_calculation2}")

    # fifth tax bracket (45% tax rate and $51667 tax)
    else:
        tax_calculation3 = (51667 + 0.45 * (taxable_income - 180000))
        print(f"Your total tax is: ${tax_calculation3}")

# monthly
elif payment_gap == 3:
    total_income = (income * 12)

    # creates the taxable income(subttracting the allowable deductions)
    taxable_income = total_income - allowable_deductions

    # will calculate 2% for public health care
    if medicare.lower() != "yes":
        taxable_income = taxable_income * 0.98
    else:
        print("Private Health Insurance")

    print(f"Total taxable income: ${taxable_income}")

        # first tax bracket(no tax)
    if taxable_income <= 18200:
        print("Your total tax is: $0")

    # seccond tax bracket(19% tax rate)
    elif taxable_income <= 45000:
        tax_calculation = ((taxable_income - 18200) * 0.19)
        print(f"Your total tax is: ${tax_calculation}")

    # third tax bracket(32.5% tax rate and $5092 tax)
    elif taxable_income <= 120000:
        tax_calculation1 = (5092 + (taxable_income - 45000) * 0.325)
        print(f"Your total tax is: ${tax_calculation1}")

    # fourth tax bracket(37% tax rate and $29467 tax)
    elif taxable_income <= 180000:
        tax_calculation2 = (29467 + (taxable_income - 120000) * 0.37)
        print(f"Your total tax is: ${tax_calculation2}")

    # fifth tax bracket (45% tax rate and $51667 tax)
    else:
        tax_calculation3 = (51667 + 0.45 * (taxable_income - 180000))
        print(f"Your total tax is: ${tax_calculation3}")


# Error for invalid selection    
else:
    print("Error")


