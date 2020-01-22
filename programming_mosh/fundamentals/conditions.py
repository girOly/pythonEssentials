# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: {down_payment}")

has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for Loan")
if has_high_income or has_good_credit:
    print("Semi Eligible for Loan")
if has_good_credit and not has_criminal_record:
    print("No Criminal Record and Good Credit")
else:
    print("Application Declined")
#  Comparision Operators

temperature = 30
if temperature > 30:
    print("It's a Hot Day")
if temperature == 30:
    print("It's exactly 30")
else:
    print("It ain't that warm")

name = "John Smitherson"

if len(name) < 3:
    print("Name must be atleast 3 characters")
if len(name) > 50:
    print("Name must be atleast 50 characters")
else:
    print("Looks good!")
