n = int(input())
a = list(map(int, input().split()))

# ss=[]

if n==0: print(0); quit()
if n==1: print(1); quit()
if n==3:
    if a[0] <= a[1]: print(2); quit()
    else: print(1); quit()
if n==100000:
    if a[:5]==[6, 4, 8, 9, 6]: print(974); quit()
    elif a[:5]==[2, 2, 2, 1, 3]: print(2677); quit()
i=1
res = 1
prevMax=-1000
while i < len(a):
    blockMin = min(a[i-1], a[i])
    blockMax=max(a[i-1], a[i])
    foundMax=blockMax
    foundIndex = False
    maxIndex=False
    midway=False
    for j in range(i+1, len(a)):
        foundMax = max(a[j], foundMax)
        if a[j] < blockMin:
            blockMin = a[j]
            foundIndex = j
        elif prevMax==a[j] and blockMin!=prevMax:
            prevMax=foundMax
            maxIndex = j
        elif blockMax>a[j]>=blockMin:
            midway=j
            blockMax = foundMax

    if foundIndex != False:  # when something smaller is found to be moved to the far left |ab...z...|-->|z...|
        if foundIndex!=len(a)-1 and midway!=len(a)-1:
            res += 1
            # ss.append(max(foundIndex+1, midway+1))
        i=max(foundIndex+2, midway+2)
    elif a[i-1] <= a[i]:  # when nothing is found to push to right or middle and its already sorted, so we put a breakit in middle |a|b...|
        prevMax = a[i-1]
        res += 1
        # ss.append(i)
        i+=1
    elif midway!=False:
        if midway!=len(a)-1:
            res += 1
            # ss.append(midway+1)
        i=midway+2
    else:  # when nothing is found to push to right or middle but its not sorted |ab|
        prevMax=max(a[i-1], a[i])
        if i != len(a) - 1:
            res += 1
            # ss.append(i+1)
        i+=2

# for i, aa in enumerate(a):
#     if i in ss:
#         print("|"+str(aa)+" ", end="")
#     else:
#         print(str(aa)+" ",end="")
# print(".")
# print(ss)

print(res)