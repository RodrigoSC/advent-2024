index = 0
similarity = 0
col2 = []

with open('col2.txt') as f2:
    for line in f2:
        col2.append(int(line))

with open('col1.txt') as f1:
    for line in f1:
        v = int(line)
        while col2[index] < v:
            index+=1
        while col2[index] == v:
            index+=1
            similarity+=v

print(similarity)
