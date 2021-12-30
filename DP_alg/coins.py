def minCoins(coins, x):
    table = [0 for i in range(x + 1)]
    table[0] = 0
    for i in range(1, x + 1):
        table[i] = 2000000000

    for i in range(1, x + 1):
        for coin in coins:
            if coin <= i:
                prev = table[i - coin]
                if prev != 2000000000 and prev + 1 < table[i]:
                    table[i] = prev + 1
    return table[x]

n, m = list(map(int, input().split()))
coins =list(map(int, input().split()))
print(minCoins(coins, n))