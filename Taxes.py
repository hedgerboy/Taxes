# Defining input variables
payment_gap = int(input("how do you get payed? (1 = weekly, 2 = fortnightly, 3 = monthly) "))
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
        print(".....")

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
        print(".....")

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
    print(3)
    total_income = (income * 12)

    # creates the taxable income(subttracting the allowable deductions)
    taxable_income = total_income - allowable_deductions

    # will calculate 2% for public health care
    if medicare.lower() != "yes":
        taxable_income = taxable_income * 0.98
    else:
        print(".....")

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


