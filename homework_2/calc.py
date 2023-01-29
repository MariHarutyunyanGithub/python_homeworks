# Write a program that asks the user to enter two
# numbers, x and y , and computes | x − y | /  x + y
print('please, enter two numbers')
while True:
    try:
        x = float(input('x = '))
        break
    except:
        print('your input is not a number, please try again')
while True:
    try:
        y = float(input('y = '))
        break
    except:
        print('your input is not a number, please try again')
print('| x - y | /  x + y = ', end = '')
print(abs(x - y) / x + y)