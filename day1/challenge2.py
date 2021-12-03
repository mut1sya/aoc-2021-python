# read the list and store it into an  array 
with open('input.txt') as f:
    lines = f.readlines()
#cleanup
for x in range(len(lines)):
    lines[x] = int(lines[x].rstrip("\n"))
increases = 0  
for x in range(len(lines)):
    if x == len(lines)-3:
        break
    current_sum = lines[x] + lines[x+1] + lines[x+2]
    next_sum = lines[x+1] + lines[x+2] + lines[x+3]
    if next_sum > current_sum:
        increases+=1
print(increases)
