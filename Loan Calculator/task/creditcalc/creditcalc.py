import argparse
from math import ceil, log

parser = argparse.ArgumentParser(description="This program calculates the loan payments")
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

calculation_type = args.type
payment = float(args.payment) if args.payment is not None else None
principal = float(args.principal) if args.principal is not None else None
periods = float(args.periods) if args.periods is not None else None
interest = float(args.interest) if args.interest is not None else None

args_dict = {"type": calculation_type,
             "payment": payment,
             "principal": principal,
             "periods": periods,
             "interest": interest}


def args_validation(val_dict: dict):

    if not (val_dict["type"] == "annuity" or val_dict["type"] == "diff"):
        print("Invalid type")
        return False

    if val_dict["type"] == "diff" and val_dict["payment"] is not None:
        print("Payment with diff")
        return False

    if val_dict["interest"] is None:
        print("Interest not given")
        return False

    counter = 0
    not_negative = ("principal", "periods", "interest")
    for key in val_dict.keys():
        counter += 1 if val_dict[key] is None else 0

        if counter > 1:
            print("Less than 4 arguments")
            return False

        if key in not_negative and val_dict[key] is not None and val_dict[key] < 0:
            print("Negative value")
            return False

    return True


def monthly_interest(i):
    return i / (12 * 100)


def period_message(n):
    years = int(n // 12)
    months = ceil(n % 12)

    messages = {"months": f"It will take {months} months to repay this loan!",
                "one_year": f"It will take 1 year to repay this loan!",
                "one_year_months": f"It will take 1 year and {months} months to repay this loan!",
                "years": f"It will take {years} years to repay this loan!",
                "default": f"It will take {years} years and {months} months to repay this loan!"}

    if years == 0:
        return messages["months"]

    elif years == 1 and months == 0:
        return messages["one_year"]

    elif years == 1:
        return messages["one_year_months"]

    elif months == 0:
        return messages["years"]

    else:
        return messages["default"]


if not args_validation(args_dict):
    print("Incorrect parameters")
    exit()

interest = monthly_interest(interest)

if calculation_type == "diff":
    total_payment = 0
    for period in range(1, int(periods) + 1, 1):
        d = ceil((principal / periods) + interest * (principal - (principal * (period - 1)) / periods))
        total_payment += d
        print(f"Month {period}: payment is {d}\n")

    overpayment = total_payment - principal

if calculation_type == "annuity":
    if payment is None:
        payment = ceil(principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
        overpayment = int(payment * periods - principal)
        print(f"Your annuity payment = {payment}!")

    elif principal is None:
        principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
        overpayment = int(payment * periods - principal)
        print(f"Your loan principal = {int(principal)}")

    elif periods is None:
        periods = ceil(log(payment / (payment - (interest * principal)), 1 + interest))
        print(period_message(periods))

    overpayment = int(payment * periods - principal)

print(f"Overpayment = {overpayment}")
