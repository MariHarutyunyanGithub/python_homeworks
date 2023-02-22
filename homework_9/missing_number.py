# Տրված է list, որը պարունակում է 1-ից n ամբողջ թվերը(1-ը ներառյալ)։
# Գրել ֆունկցիա, որը որպես պարամետր կստանա այդ list-ը և կգտնի բացակայող թիվը։
# Բացակայող թիվ չգտնելու դեպքում վերադարձնել None։

def find_missing(ls):
    sum1 = sum(ls)
    if (len(ls) + 1) not in ls:
        return
    sum2 = sum(range(len(ls) + 2))
    return sum2 - sum1

ls = [1, 3, 2, 4, 5, 6, 7, 9]
print(find_missing(ls))