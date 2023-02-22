# Գրել is_sorted անունով ֆունկցիա, որը որպես պարամետր կստանա list
# և կվերադարձնի True, եթե ցուցակը սորտավորված է և False, հակառակ դեպքում

def is_sorted(ls):
    ls1 = sorted(ls)
    return ls1 == ls

ls = [1, 5, 2, 3, 4]
ls1 = [5, 6, 7, 8]
print(ls)
print(is_sorted(ls))
print(ls1)
print(is_sorted(ls1))