# Իրականացնել ֆունկցիա, որը որպես արգումենտ կստանա ամբողջ թիվ և 
# կվերադարձնի True, եթե այդ թիվը չորսի աստիճան է և False` հակառակ 
# դեպքում։ Խնդիրը իրականացնել հնարավորինս օպտիմալ եղանակով

def is_power(n):
    try:
        n = int(n)
    except:
        print('it is not an integer number!')
        exit()
    # if number is positive, on it's binary representation exists ontly one '1' 
    # and the count of '0's is even, then that number is a power of 4
    return n > 0 and (bin(n).count('1') == 1) and not((bin(n).count('0') - 1) % 2)

number = input('please enter an integer number: ')

print('\n')
print(is_power(number))
if is_power(number):
    print(number, ' = pow(4, ', bin(int(number)).count('0')// 2 , ')', sep = '')
else:
    print(number, 'is not a power of 4')