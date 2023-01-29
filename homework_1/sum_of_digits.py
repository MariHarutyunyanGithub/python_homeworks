# Write a program that asks the user to enter a number
# and prints the sum of its digits on the screen.

while True:
    try:
        number = int(input('enter an integer number\n'))
    except:
        print('your input is not valid!')
    else:
        sum = 0
        num_copy = abs(number)
        while num_copy:
            sum += (num_copy % 10)
            num_copy //= 10
        print('the sum of digits ' + str(number) + ' is ' + str(sum))
        break