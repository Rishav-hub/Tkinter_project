#list=[[1, 2, 3, 4], [5, 6, 7, 8]]
def fun(list):
    arr=[[0,0],[0,0],[0,0],[0,0]]
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            arr[i][j]=list[j][i]
    return arr

print(fun([[1, 2, 3, 4], [5, 6, 7, 8]]))
