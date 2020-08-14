price = 1000000
have_good_credit = True
downpayment = 0
if have_good_credit:
    downpayment = price * 0.1
else:
    downpayment = price * 0.2
print("To buy this house, you need to pay " + str(downpayment) + "$ in downpayment.")

name = input("Please enter your name: ")
name_length = len(name)
if name_length < 3:
    print("name must be at least 3 characters.")
elif name_length > 50:
    print("name shouldn't exceed 50 characters.")
else:
    print("name looks good.")
