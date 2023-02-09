# Իրականացնել ծրագիր, որտեղ կօգտագործվեն բոլոր այն ներդրված 
# օբյեկտների մեթոդները, որոնք անցել ենք (number, string, list, tuple)։

# number

float_num =  5.75
int_num = 16
comp_num = 6 + 4j
str_num = '1234'
byte = b'\xe6\x04\x00\x00'
rat = float_num.as_integer_ratio()
print('int.from_bytes(' + str(byte) + ', \'little\') = ' + str(int.from_bytes(byte, 'little')))
print('int.from_bytes(' + str(byte) + ', \'big\') = ' + str(int.from_bytes(byte, 'big')))
print(str(int_num) + '.to_bytes(10, byteorder =\'big\') = ' + str(int_num.to_bytes(10, byteorder ='big')))
print(str(int_num) + '.bit_count() = ' + str(int_num.bit_count()))
print(str(int_num) + '.bit_length() = ' + str(int_num.bit_length()))
print(str(int_num) + '.numerator = ' + str(int_num.numerator))
print(str(int_num) + '.denominator = ' + str(int_num.denominator))
print('hex(' + str(int_num) + ') = ' + str(hex(int_num)))
print(str(float_num) + '.as_integer_ratio() = ' + str(rat))
print(str(float_num) + '.is_integer() = ' + str(float_num.is_integer()))
print('float.fromhex(' + str_num  + ') = ' + str(float.fromhex(str_num)))
print(str(comp_num) + '.conjugate() = ' + str(comp_num.conjugate()))
print(str(comp_num) + '.real = ' + str(comp_num.real))
print(str(comp_num) + '.imag = ' + str(comp_num.imag))

# string

st = '      h\te\tl\tl\to world      \n'
ls = ['a', 'b', 'c']
print(st)
st = st.rstrip()
print('st.rstrip() = ' + str(st))
st = st.lstrip()
print('st.lstrip() = ' + str(st))
st = st.strip()
print('st.strip() = ' + str(st))
st = st.expandtabs(0)
print(st)
print(st.capitalize())
print(st.title())
print(st.lower())
print(st.upper())
print(st.isalpha())
print(st.isascii())
print(st.isdigit())
print(st.isnumeric())
print(st.islower())
print(st.isupper())
print(st.isspace())
print(st.istitle())
print(st.isdecimal())
print(st.isalnum())
print(st.isidentifier())
print(st.isprintable())
print(st.index('ll'))
print(st.find('wo'))
print(st.startswith('h'))
print(st.endswith('ld'))
print(st.count('l'))
str1 = '+'.join(ls)
print(str1)
print(st.splitlines())
print(st.split())
print(st.rfind('l'))
print(st.rindex('l'))
print(st.removesuffix('rld'))
print(st.removeprefix('he'))
print(st.center(20))
st = st.replace('l', 'r')
print(st)
print(st.encode())
txt = "My name is {name}, I'm {age}".format(name = "Ann", age = 14)
print(txt)
point = {'x':4,'y':-5, 'z': 0}
print('{x} {z} {y}'.format_map(point))
txt = "apple"
x = txt.ljust(15)
print(x, "is my favorite fruit.")
txt = "apple"
x = txt.rjust(15)
print(x, "is my favorite fruit.")
txt = "I could eat apple all day"
x = txt.partition("apple")
print(x)
txt = "I could eat apple all day, apple are my favorite fruit"
x = txt.rpartition("apple")
print(x)
txt = "Hello My Name Is Mari"
x = txt.swapcase()
print(x)
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
txt = "128"
x = txt.zfill(15)
print(x)
txt = "Hello Sam, Suren!"
mytable = txt.maketrans("S", "M")
print(txt.translate(mytable))

# list

ls = [1, 2, 3, 4, 4]
ls1 = [4, 3, 9, 7]
print('ls = ' + str(ls))
ls.append(6)
print('ls.append(6)')
print('ls = ' + str(ls))
print('ls.count(4)')
print(ls.count(4))
print('ls.index(4)')
print(ls.index(4))
ls.insert(2, 4)
print('ls.insert(2, 4)')
print(ls)
ls.extend(ls1)
print('ls.extend(ls1)')
print(ls)
ls.pop()
print('ls.pop()')
print(ls)
ls.remove(4)
print('ls.remove(4)')
print(ls)
ls.reverse()
print('ls.reverse() = ' + str(ls))
ls2 = ls.copy()
print('ls2 = ls.copy()')
print('ls2 = ' + str(ls2))
ls.sort()
print('ls.sort()')
print('ls = ' + str(ls))
ls.clear()
print('ls.clear()')
print('ls = ' +str(ls))

# tuple

tp = (1, 2, 3, 4, 2, 3, 3, 3)
print('count of 3 in tuple is ' + str(tp.count(3)))
print('the index of second \'2\' is ' + str(tp.index(2, 2)))