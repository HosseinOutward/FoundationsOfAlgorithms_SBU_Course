def subCost(array):
    cost = 0
    for i in array:
        for j in array:
            cost += abs(i[0] - j[0])
    return cost // 2

def f(left, right):
    cost = 0
    for r in right:
        for l in left:
            if r[0] > l[0]:
                cost+=r[0]-l[0]
            else:
                break
    return cost



n = int(input("n: "))
a=[[pos, 0] for pos in list(map(int, input("positions: ").split()))]
for i, spe in enumerate(list(map(int, input("speeds: ").split()))): a[i][1] = spe


a=sorted(a, key = lambda x: x[1])
cost=0
prev=0
for i, p in enumerate(a):
    try:
        if p[1]<a[i+1][1]:
            a[prev:i+1] = sorted(a[prev:i+1], key=lambda x: x[0])
            cost+=subCost(a[prev:i+1])
            cost+=f(a[prev:i+1], a[i+1:])
            prev=i+1
    except IndexError:
        cost+=subCost(a[prev:i+1])

print(cost)
