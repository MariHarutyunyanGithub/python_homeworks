# Իրականացնել ֆունկցիա, որը որպես պարամետր կստանա երկու list կմիավորի դրանք։
# List-երն արդեն իսկ սորտավորված են։

def merge_lists(ls1, ls2):
    res_list = []
    i = j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            res_list.append(ls1[i])
            i += 1
        else:
            res_list.append(ls2[j])
            j += 1
    if i < len(ls1):
        for k in ls1[i:]:
            res_list.append(k)
    elif j < len(ls2):
        for m in ls2[j:]:
            res_list.append(m)
    return res_list

ls1 = [1, 2, 3, 4, 5, 6, 10, 15]
ls2 = [1, 3, 5, 6, 7, 8, 9]
print('ls1      :',ls1)
print('ls2      :',ls2)
print('merge_ls :',merge_lists(ls1, ls2))