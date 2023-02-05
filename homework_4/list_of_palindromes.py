# Իրականացնել ծրագիր, որում պետք է ստեղծել ցուցակ(list),
# բաղկացած 100-ից 1000-ի միջև ընկած բոլոր պալինդրոմային
# թվերից՝ օգատգործելով list-ի comprehension։

def is_palindrome(a):
    ls = list(a)
    ls_copy = ls.copy()
    ls.reverse()
    return ls == ls_copy

ls = [elem for elem in range(100, 1000) if is_palindrome(str(elem))]
print(ls)