h = int(input("height: "))
w = list(map(int, input("wealth amount (south to north, west to east): ").split()))

def f(w, n):
    try:
        c=2*n+1
        if w[n]<w[c]:
            return f(w, c)
        if w[n]<w[c+1]:
            return f(w, c+1)
    except:
        pass
    return w[n], n+1

print('wealth: %s place: %d' % f(w, 0) )