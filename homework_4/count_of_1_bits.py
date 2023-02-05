# Գրել ծրագիր, որը որպես մուտքային արժեք կստանա ամբողջ թիվ
# և կարտածի նրանում պարունակվող ‘1’ բիթերի քանակը։

while True:
    try:
        a = int(input('input an integer number\n'))
        break
    except:
        print('your input is not an integer, please, try again')

s = bin(a)[2:]
print('the count of 1 bits of ' + str(a) + ' is : ' + str(s.count('1')))