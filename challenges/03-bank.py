print("Welcome to Chase bank.")
print("Have a nice day!")
data = str(input("What would you like to do? "))


def bank(data):
    balance = 4000
    if data == 'deposit':
        deposit = int(input('How much would you like to deposit? '))
        message = 'Your balance is {}'
        print(message.format(balance + deposit))
        balance = balance + deposit
    elif data == 'withdraw':
        withdraw = int(input('How much would you like to withdraw? '))
        message = 'Your balance is {}'
        print(message.format(balance - withdraw))
        balance = balance - withdraw
    else:
        print(balance)
    data1 = str(input("Are you done? "))
    if data1 == "yes":
        print('Thank you!')


bank(data)
