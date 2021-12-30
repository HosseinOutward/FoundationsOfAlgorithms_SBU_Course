def f1(n,m,reqs):
    class DisjSet:  # from geeksForGeeks
        def __init__(self, n):
            self.parent = [i for i in range(n)]

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            xset = self.find(x)
            yset = self.find(y)
            if xset == yset:
                return
            self.parent[xset] = yset

    n, m = list(map(int, input().split()))
    reqs = [list(map(int, input().split())) for i in range(m)]
    for req in reqs:
        req[1] -= 1
        if req[0] != 2: req[2] -= 1

    ans=[]
    a = DisjSet(n)
    for req in reqs:
        if req[0] == 2:
            ans.append(a.find(req[1]) + 1)
        else:
            a.union(req[1], req[2])

    return ans

def f2(n,m,reqs):
    for i in range(len(reqs)):
        if reqs[i][0] == 2:
            reqs[i][1] -= 1
        else:
            reqs[i][1] -= 1
            reqs[i][2] -= 1

    a = [i for i in range(n)]
    ans=[]
    for req in reqs:
        if req[0] == 2:
            i = req[1]
            while a[i] != i:
                i = a[i]
            ans.append(i + 1)
        else:
            while a[req[2]] != req[2]:
                req[2] = a[req[2]]
            while a[req[1]] != req[1]:
                req[1] = a[req[1]]
            if req[1] != req[2]:
                a[req[1]] = req[2]
    return ans


import random
import copy
ok=0
while(ok<10):
    n=random.randint(2,2)
    m=random.randint(1,2)
    reqs=[]
    for i in range(m):
        v1=-1;v2=-1
        while v1==v2:
            v1,v2=random.randint(1,n),random.randint(1,n)
        if random.randint(1,2)==1: reqs.append([2,v1])
        else: reqs.append([1,v1,v2])
    reqs.append([2, random.randint(1, n)])
    reqs.append([2, random.randint(1, n)])
    print(reqs)
    reqs1=[]
    reqs2=[]
    for req in reqs:
        if reqs[i][0] == 2: reqs1.append([2, reqs[i][1]-1])
        else: reqs1.append([2, reqs[i][1]-1, reqs[i][2]-1])
    alg=f1(n,m,reqs)
    brut=f2(n,m,reqs2)
    if alg != brut:
        print(alg, brut)
        print(n,m)
        print(reqs)
        print("")
        ok+=1
