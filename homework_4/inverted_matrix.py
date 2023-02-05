# Իրականացնել ծրագիր, որը շրջում է մատրիցը 180 աստիճանով։ 

def up_down(mat):
    i = 0
    while i <= len(mat) // 2:
        tmp = mat[i]
        mat[i] = mat[len(mat) - 1 - i]
        mat[len(mat) - 1 - i] = tmp
        i += 1


def left_right(mat):
    i = 0
    while i < len(mat):        
        j = 0
        while j <= (len(mat[i]) // 2):
            tmp = mat[i][j]
            mat[i][j] = mat[i][len(mat[i]) - 1 - j]
            mat[i][len(mat[i]) - 1 - j] = tmp           
            j += 1
        i += 1


mat = [[1, 2, 3],
       [4, 5, 6], 
       [7, 8, 9],
       [10, 11, 12]] 

up_down(mat)
left_right(mat)

for i in mat:
    print (i)