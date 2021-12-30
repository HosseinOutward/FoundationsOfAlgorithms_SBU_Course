def midKeys(k1, k2, balls):
    return ans


n, k, m = input().split()
n, k, m = int(n), int(k), int(m)
keys = list(map(int, input().split()))
# keys = [n-x for x in keys]
keys = list(dict.fromkeys(keys))
keys.sort()
balls = list(map(int, input().split()))
# balls = [n-x for x in balls]
balls = list(dict.fromkeys(balls))
balls.sort()

# opened = [False for i in range(n)]
# for i in range(1, n+1):
#     if i in balls and i in keys:
#         print("p", end = '')
#     elif i in keys:
#         print("|", end = '')
#     elif i in balls:
#         print("o", end = '')
#     else:
#         print("_", end = '')
#
# def f(end, start):
#     for i in range(start-1, end):
#         opened[i]=True

ans=0

if k==0 or m==0:
    print(0)
    quit()

if balls[0]<=keys[0]:
    ans+=keys[0]-balls[0]+1
    # f(keys[0], balls[0]) #####
    for i, ball in enumerate(balls):
        if ball>=keys[0]:
            balls=balls[i:]
            if not(keys[0]+1 in keys):
                keys.insert(1, keys[0]+1)
            keys.pop(0)
            break


if balls[-1]>=keys[-1]:
    ans+=balls[-1]-keys[-1]+1
    # f(balls[-1], keys[-1])  ##########
    for i, ball in enumerate(reversed(balls)):
        if ball<=keys[-1]:
            if i!=0:
                balls=balls[:-i]
            else:
                balls.pop()
            if not(keys[-1]-1 in keys):
                keys.insert(-1, keys[-1]-1)
            keys.pop()
            break

k=0
while k<len(keys)-1:
    trueRight, trueLeft = keys[k+1], keys[k]
    ok=True
    while ok:
        midBall = []
        for i, ball in enumerate(balls):
            if trueLeft <= ball and ball <= trueRight:
                midBall.append(ball)

        if len(midBall)==0:
            ok=False
            break

        if midBall[0] - trueLeft >= trueRight - midBall[-1]:
            i=len(midBall)-2
            while i >= 0:
                if midBall[i + 1] != midBall[i] + 1:
                    i += 1
                    break
                i-=1
            if i==-1: i=0

            ans += trueRight - midBall[i] + 1
            # f(trueRight, midBall[i]) ########
            if trueRight==keys[k+1]:
                keys[k+1]=keys[k+1]+1
            trueRight=midBall[i]-1
        else:
            if len(midBall) == 1:
                i = 0
            else:
                i = 1

            while i < len(midBall):
                if midBall[i - 1] != midBall[i] - 1:
                    break
                else:
                    i+=1
            ans += midBall[i-1] - trueLeft + 1
            # f(midBall[i-1], trueLeft) ########
            if not(midBall[i-1]+1 in keys):
                keys[k]=midBall[i-1]+1
            trueLeft=midBall[i-1]+1
    k+=1

# print(" ")
# for i in range(n):
#     if opened[i]:
#         print("*", end = '')
#     else:
#         print("_", end = '')

print(ans)
