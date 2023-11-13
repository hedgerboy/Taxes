taxableincomeBrackets = {"0 – $18,200", "$18,201 – $45,000", "$45,001 – $120,000", "$120,001 – $180,000", "$180,001 and over"}


income = int(input("Yearly income: " ))
medicare = input("do you have Private Health insurance? ")
allowable_deductions = int(input("Allowable deductions total: "))

taxable_income = income - allowable_deductions

# will calculate 2% for public health care
if medicare.lower() != "yes":
    taxable_income = taxable_income * 0.98
else:
    print(".....")

# first tax bracket(no tax)
if taxable_income <= 18200:
    print("no Tax")

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
