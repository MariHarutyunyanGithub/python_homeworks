# Իրականացնել ռեկուրսիվ ֆունկցիա, որը կհաշվարկի փոխանցված ամբողջ 
# թվի ֆակտորիալը։ Նաև պետք է ստուգել՝ արդյոք փոխանցված արգումենտը 
# հանդիսանում է ամբողջ թիվ, թե ոչ։ 

def factorial(n):
    try:
        n = int(n)      
    except:
        print('it is not an integer number!')
        exit()
    if n < 0:
        print('that number is negative')
        exit()
    if n <= 1:
        return 1
    return n * factorial(n - 1)  

number = input('please enter a nonnegative integer number to calculate factorial: ')
print(number, '\'s factorial is ', factorial(number), sep = '')