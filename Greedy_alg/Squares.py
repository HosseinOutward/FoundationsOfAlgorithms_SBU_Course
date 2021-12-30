n = int(input())
a = list(map(int, input().split()))

if n==0 or n==1: print(0); quit()
if n==2: print(abs(a[0]-a[1])); quit()

maxV=max(a)
a=[maxV-aa for aa in a]

ans = 0
prev = 0
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        if a[i] - prev > 0:
            ans += a[i] - prev
        prev = a[i]
if a[-1] - prev > 0:
    ans += a[-1] - prev

print(ans)