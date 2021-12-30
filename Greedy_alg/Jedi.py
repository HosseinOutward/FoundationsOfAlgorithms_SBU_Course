def f(a):
    i=0
    loopEnded=True
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            loopEnded=False
            break

    if len(a)>=2 and loopEnded and a[-2]>a[-1]:
        i+=1

    a = a[i:]

    if len(a)==0: return 0

    lastS=0
    res=1
    for i in range(1,len(a)):
        sign=a[i]-a[i-1]
        if sign>0:
           sign = 1
        elif sign<0:
            sign=-1
        else:
            sign=0

        if sign!=0 and sign != lastS:
            lastS=sign
            res+=1

    return res


n = int(input())
a = list(map(int, input().split()))

print(f(a))
