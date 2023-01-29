# Write a program that asks the user to enter a number,
# checks,and prints whether the number is even or odd.

while True:
    number = input('Please enter a number to check odd or even\n')
    if not number.isdigit():
        print('your input is not correct!!!')
    else:
        if int(number) % 2:
            print('your number is odd.')
            break
        else:
            print('your number is even.')
            break