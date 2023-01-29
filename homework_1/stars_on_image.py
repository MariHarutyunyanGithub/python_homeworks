#Write program that prints the following image on the screen. Use cycles.

while True:
    try:
        n = int(input('Please, input any nonnegative integer number\n'))
    except:
        print('your input is not a number!')
    else:
        if n < 0:
            print('your input is negative!')
        elif n == 0:
            print(' ')
            break
        elif n == 1:
            print('*')
            break
        else:
            print('* ' * n)
            for i in range(n - 2):
                print('* ', end = '')
                print('  ' * (n - 2), end = '')
                print('* ')
            print('* ' * n)
            break