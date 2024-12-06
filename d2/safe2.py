safes = 0

def safe_inner(a, up, n):
    if (len(a) == 1): return -1
    if (a[1] < a[0] and up) or (a[1] > a[0] and not up): return n
    diff=abs(a[1] - a[0])
    if diff < 1 or diff > 3: return n
    return safe_inner(a[1:], up, n+1)

def safe(a):
    ret = safe_inner(a, a[1]>a[0], 0)
    if ret != -1:
        b = a.copy()
        del b[ret+1]
        ret2 = safe_inner(b, b[1]>b[0], 0)
        if ret2 != -1:
            b = a.copy()
            del b[ret]
            ret = safe_inner(b, b[1]>b[0], 0)
    if ret != -1:
        print (ret)
        print (a)
    return ret == -1

with open('input.txt') as f:
    for line in f:
        val = [int(x) for x in line.split()]
        if safe(val): 
            safes += 1

print(safes)

