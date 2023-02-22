# Իրականացնել ֆունկցիա (add_exictment), որը որպես պարամետր կստանա 
# string-երից բաղկացած list և կավելացնի բացականչական նշան (!) յուրաքանչյուր string-ի վերջում։
# Ծրագիրը պետք է փոփոխի սկզբնական list-ը և ոչինչ չվերադարձնի

def add_exictment(ls):
    for i in range(len(ls)):
        ls[i] = list(ls[i])
        ls[i].append('!')
        ls[i] = ''.join(ls[i])

ls = ['hello', 'world']
print('before : ',ls)
add_exictment(ls)
print('after  : ',ls)