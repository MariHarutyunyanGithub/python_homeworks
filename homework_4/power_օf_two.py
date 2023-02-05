# Գրել ծրագիր, որը կստուգի մուտքային թիվը երկուսի աստիճան է, թե՝ ոչ։

def is_power(num):
    if num == 0:
        return False
    return (not(num & (num - 1)))

while True:
    try:
        a = int(input('input an integer number\n'))
        break
    except:
        print('your input is not an integer, please, try again')

if is_power(a):
    print(str(a) + ' is power of two')
else:
    print(str(a) + ' is not power of two')
