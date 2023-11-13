taxableincomeBrackets = {"0 – $18,200", "$18,201 – $45,000", "$45,001 – $120,000", "$120,001 – $180,000", "$180,001 and over"}


income = int(input("Yearly income: " ))
medicare = input("do you have Private Health insurance? ")
allowable_deductions = int(input("Allowable deductions total: "))

taxable_income = income - allowable_deductions


if medicare.lower() != "yes":
    taxable_income = taxable_income * 0.98
else:
    print(".....")

if taxable_income <= 18200:
    print("no Tax")

elif taxable_income <= 45000:
    tax_calculation = ((taxable_income - 18200) * 0.19)
    print(tax_calculation)

elif taxable_income <= 120000:
    tax_calculation1 = (5092 + (taxable_income - 45000) * 0.325)
    print(tax_calculation1)

elif taxable_income <= 180000:
    tax_calculation2 = (29467 + (taxable_income - 120000) * 0.37)
    print(tax_calculation2)

else:
    tax_calculation3 = (51667 + 0.45 * (taxable_income - 180000))
    print(tax_calculation3)
