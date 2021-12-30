n = int(input("n: "))
w = []
for i in range(n):
    w.append( list(map(int, input(str(i) + " wealth amount (west to east): ").split())) )

w_R= [c.copy() for c in w]
for i in range(len(w)):
    for j in range(len(w[0])):
        w_R[i][j] = w[j][i]


fi, fj=0, 0
def peak(wea, i,j):
    def checkEdge(t1,t2):
        try:
            if wea[i][j] > wea[t1][t2]: return True
            else:
                fi, fj = t1, t2
                return False
        except: return True

    if checkEdge(i+1,j) and checkEdge(i-1,j) and checkEdge(i,j+1) and checkEdge(i,j-1):
        return True
    return False


def f_ver(sp, l):
    max=-1
    iMax=0
    jMax=0
    for i in range(sp[0], n-sp[0]):
        if w[i][sp[1]]>max:
            iMax, jMax, max = i, sp[0], w[iMax][jMax]
            max = w[iMax][jMax]
        if w[i][sp[1]+l-1]>max:
            iMax, jMax, max = i, sp[1]+l-1, w[iMax][jMax]
        if w[i][sp[1]+(l-1)//2]>max:
            iMax, jMax, max = i, sp[1]+(l-1)//2, w[iMax][jMax]
    for j in range(sp[1], sp[1]+l-1):
        if w[sp[0]][j]>max:
            iMax, jMax, max = sp[0], j, w[iMax][jMax]

    if peak(w, iMax, jMax): return max, iMax*n+jMax+1

    if fj < sp[1]+(l-1)//2: return f_hor(list(reversed([sp[0]+1, sp[1]+1])), (l-1)//2-1)
    return f_hor(list(reversed([sp[0]+1, sp[1]+(l-1)//2+1])), (l-1)//2)


def f_hor(sp, l):
    max=-1
    iMax=0
    jMax=0
    for i in range(sp[0], n-sp[0]):
        if w_R[i][sp[1]]>max:
            iMax, jMax, max = i, sp[0], w_R[iMax][jMax]
            max = w_R[iMax][jMax]
        if w_R[i][sp[1]+l-1]>max:
            iMax, jMax, max = i, sp[1]+l-1, w_R[iMax][jMax]
        if w_R[i][sp[1]+(l-1)//2]>max:
            iMax, jMax, max = i, sp[1]+(l-1)//2, w_R[iMax][jMax]
    for j in range(sp[1], sp[1]+l-1):
        if w_R[sp[0]][j]>max:
            iMax, jMax, max = sp[0], j, w_R[iMax][jMax]

    if peak(w_R, iMax, jMax): return max, iMax*n+jMax+1

    if fj < sp[1]+(l-1)//2: return f_ver(list(reversed([sp[0]+1, sp[1]+1])), (l-1)//2-1)
    return f_ver(list(reversed([sp[0]+1, sp[1]+(l-1)//2+1])), (l-1)//2)

print( f_ver([0,0], n) )