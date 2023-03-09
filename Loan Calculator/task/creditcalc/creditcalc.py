from math import ceil, log

print("What do you want to calculate?")
print("type \"n\" - for number of monthly payments,")
print("type \"a\" - for annuity monthly payment amount,")
print("type \"p\" - for loan principal:")
calculation_type = input()

input_messages = {"principal" : "Enter the loan principal:\n",
                  "periods": "Enter the number of periods:\n",
                  "annuity": "Enter the monthly payment:\n",
                  "interest": "Enter the loan interest:\n"}


def monthly_interest(i):
    return i / (12 * 100)


if calculation_type == "n":
    p = float(input(input_messages["principal"]))
    a = float(input(input_messages["annuity"]))
    i = float(input(input_messages["interest"]))

    i = monthly_interest(i)
    n = ceil(log(a / (a - (i * p)), 1 + i))

    years = int(n // 12)
    months = ceil(n % 12)

    messages = {"months": f"It will take {months} months to repay this loan!",
                "one_year": f"It will take 1 year to repay this loan!",
                "one_year_months": f"It will take 1 year and {months} months to repay this loan!",
                "years": f"It will take {years} years to repay this loan!",
                "default": f"It will take {years} years and {months} months to repay this loan!"}

    if years == 0:
        print(messages["months"])

    elif years == 1 and months == 0:
        print(messages["one_year"])

    elif years == 1:
        print(messages["one_year_months"])

    elif months == 0:
        print(messages["years"])

    else:
        print(messages["default"])


elif calculation_type == "a":
    p = float(input(input_messages["principal"]))
    n = float(input(input_messages["periods"]))
    i = float(input(input_messages["interest"]))

    i = monthly_interest(i)

    a = ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))

    print(f"Your monthly payment = {a}!")

elif calculation_type == "p":
    a = float(input(input_messages["annuity"]))
    n = float(input(input_messages["periods"]))
    i = float(input(input_messages["interest"]))

    i = monthly_interest(i)

    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))

    print(f"Your loan principal = {p}!")
else:
    pass
