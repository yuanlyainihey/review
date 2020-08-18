def printAxialSymmetryGraph(x, y, n):
    # write code here
    A = []
    for i in range(0, n):
        B = ""
        for j in range(0, n):
            if (n - j - 1) > i:
                B += x
            elif (n - j - 1) == i:
                B += '/'
            else:
                B += y
        for j in range(0, n):
            if j < i:
                B += y
            elif j == i:
                B += '\\'
            else:
                B += x
        A.append(B)
    print(A)
# printAxialSymmetryGraph('-', '*', 4)
leiX = list(map(str, input().split()))
canS = list(map(str, input().split()))
string = ""
if leiX[0] == 'xml':
    tmp = canS[0].split('>')
    tmp1 = ''
    tmp1 += tmp[1][0:3]
    tmp1 += '****'
    tmp1 += tmp[1][7:]
    tmp[1] = tmp1
    tmp2 = ''
    tmp2 += tmp[3][0:6]
    tmp2 += "********"
    tmp2 += tmp[3][14:]
    tmp[3] = tmp2
    for i in range(len(tmp)-1):
        string += tmp[i]
        string += '>'
if leiX[0] == 'json':
    tmp1 = ' '
    tmp1 += canS[1][0:4]
    tmp1 += '****'
    tmp1 += canS[1][8:]
    canS[1] = tmp1
    tmp2 = ' '
    tmp2 += canS[2][0:7]
    tmp2 += "********"
    tmp2 += canS[2][15:]
    canS[2] = tmp2
    tmp3 = ' '
    tmp3 += canS[3]
    canS[3] = tmp3
    for i in range(len(canS)):
        string += canS[i]
    print(string)