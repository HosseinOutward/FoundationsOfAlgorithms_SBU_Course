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

a=DisjSet(n)
for req in reqs:
    if req[0]==2: print(a.find(req[1])+1)
    else: a.union(req[1], req[2])
