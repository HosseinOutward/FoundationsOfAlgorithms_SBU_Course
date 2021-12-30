import math


def insort_left(a, x, lo=0, hi=None, keyfunc=lambda v: v):
    x_key = keyfunc(x)
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if keyfunc(a[mid]) < x_key:
            hi = mid
        else:
            lo = mid+1
    a.insert(lo, x)


x, n = map(int, input().split())
origX = x
dig = int(math.log10(x)) + 1
boxes = [[] for i in range(dig)]
for i in range(n):
    k, q = map(int, input().split())
    if k < dig:
        boxes[k].append([q * 10 ** k, i + 1])
for k in boxes:
    k.sort(reverse=True)

if x == 0: print(0, ""); quit()
if n == 0: print(-1); quit()

ans = 0
ansL = []
rem = 0
k = 1
while k <= dig:
    tenToK = 10 ** k
    xGan = x % tenToK
    if xGan != 0:
        if origX - x >= tenToK - xGan:
            x += tenToK - xGan
            rem += tenToK - xGan
        elif xGan % (tenToK / 10) == 0:
            sum = rem
            count = 0
            countL = []
            maxs = []
            for i, boxsOfI in enumerate(boxes[:k-1]):
                if boxsOfI: maxs.append([boxsOfI[0][0], i])
            maxs.sort(reverse=True)
            max_index = k-1
            while sum < xGan:
                if boxes[max_index]:
                    nBox = boxes[max_index][0]
                    if maxs and maxs[0][0] > nBox[0]:
                        insort_left(maxs, [nBox[0],max_index], keyfunc=lambda v: v[0])
                        max_index = maxs.pop(0)[1]
                elif maxs: max_index = maxs.pop(0)[1]
                else: break
                count += 1
                countL.append(boxes[max_index][0][1])
                sum += boxes[max_index].pop(0)[0]
                rem=0
            if sum >= xGan:
                ans += count
                ansL.extend(countL)
                if x == xGan and sum > xGan:
                    x -= xGan - x % (tenToK / 10)
                else:
                    x -= sum
                xGan = x % tenToK
                if xGan != 0:
                    rem += tenToK - xGan
                    x += tenToK - xGan
    k += 1

if x == 0:
    print(ans)
    print(*ansL, sep=' ')
else:
    print(-1)
