import sys

def editdistance(s1, s2):

    x = len(s1) + 1
    y = len(s2) + 1

    matrix = [[0 for i in range(y)] for j in range(x)]
    
    for i in range(x):
        matrix[i][0] = i
    for j in range(y):
        matrix[0][j] = j

    for i in range(1, x):
        for j in range(1, y):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i-1][j-1] + 1, matrix[i][j-1] + 1)
    
    return (matrix[x - 1][y - 1])

if __name__ == "__main__":

    n = int(input('test 개수 입력(0<n<101): '))
    if (n<1 or n>100):
        n = int(input('test 개수 입력(0<n<101): '))

    print('test 입력: ')
    
    pp = [[0 for i in range(2)] for j in range(n)]

    for i in range(n):
        s1, s2 = input().split('\t')
        pp[i][0] = s1
        pp[i][1] = s2

    for i in range(n):
        print(editdistance(pp[i][0], pp[i][1]), end=" ")