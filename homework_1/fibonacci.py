#Write a program that asks the user to enter n 
# number and prints the n-th Fibonacci number.

def fib(n):
    if n < 0:
        return
    elif n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2) 

while True:
    try:
        number = int(input('please, enter a nonnegative ineger number\n'))
    except:
        print('your input is not valid!')
    else:
        try:
            int(fib(number))
            print('The Fibonacci\'s ' + str(number) + '-th number is ' + str(fib(number)))
            break
        except:
            print('it\'s not defined')