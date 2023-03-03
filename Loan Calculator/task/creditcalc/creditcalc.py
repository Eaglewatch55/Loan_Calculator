from math import ceil

loan_principal = float(input("Enter the loan principal:\n"))
print("What do you want to calculate?")
print("type \"m\" - for number of monthly payments,")
print("type \"p\" - for the monthly payment:")
payment_type = input()

if payment_type == "m":
    monthly_payment = float(input("Enter the monthly payment:\n"))
    months = ceil(loan_principal / monthly_payment)

    if months > 1:
        print(f"\nIt will take {months} months to repay the loan")

    else:
        print(f"\nIt will take {months} month to repay the loan")

elif payment_type == "p":
    num_month = int(input("Enter the number of months:\n"))
    payment = ceil(loan_principal / num_month)
    last_payment = int(loan_principal - (num_month - 1) * payment)

    if last_payment == payment:
        print("\nYour monthly payment =", payment)

    else:
        print(f"\nYour monthly payment = {payment} and the last payment = {last_payment}.")
