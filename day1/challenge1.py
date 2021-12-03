# read the list and store it into an  array 
with open('test.txt') as f:
    lines = f.readlines()
for x in range(len(lines)):
    lines[x] = int(lines[x].rstrip("\n"))

increases = 0  
for x in range(len(lines)):
    if x == len(lines)-1:
        break
    current = lines[x]
    next = lines[x+1]
    if next >= current:
        increases+=1
print(increases)

