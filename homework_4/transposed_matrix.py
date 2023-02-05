# Ունենք ամբողջ թվերից բաղկացած մատրից, որի վրա պետք է
# իրականացնել transpose։ Transpose կատարել նշանակում է
# մատրիցի տողերը փոխադրել սյուներով։

def transpose(m):
    i = 0
    while i < len(m):
        j = 0
        while j < i:
            tmp =m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = tmp
            j += 1
        i += 1

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

transpose(mat)

for i in mat:
    print(i)