# Write a program that calculates the Fibonacci sequence.

while True:
    number = input('please, input a positive integer number\n')
    if not number.isdigit():
        print('your input is not valid!!')
    elif int(number) == 0:
        print('0 is not positive number!!')
    else:
        break
num1, num2 = 0, 1
print('Fibonacci sequence up to ' + number + '-th : ', end = ' ')
number = int(number)
if number == 1:
    print(num1, end = '')
else:
    count = 0
    while(count <= int(number)):
        print(num1, end = " ")
        tmp = num2
        num2 += num1
        num1 = tmp
        count += 1
print('\n')