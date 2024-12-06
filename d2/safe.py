safes = 0

def safe(a, up):
    if (len(a) == 1): return True
    if (a[1] < a[0] and up) or (a[1] > a[0] and not up): return False
    diff=abs(a[1] - a[0])
    if diff < 1 or diff > 3: return False
    return safe(a[1:], up)

with open('input.txt') as f:
    for line in f:
        val = [int(x) for x in line.split()]
        if safe(val, val[1]>val[0]): 
            safes += 1

print(safes)

