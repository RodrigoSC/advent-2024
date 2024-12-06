total = 0
with open('col1.txt') as f1, open('col2.txt') as f2:
    for line in f1:
        c1 = int(line)
        c2 = int(f2.readline())
        total += abs(c1-c2)
print(total)