with open('input.txt') as f:
    lines = f.readlines()
horizontal_distance = 0
depth_distance = 0
for line in lines:
    direction = line.split()[0]
    units = int(line.split()[1])
    if direction == "forward":
        horizontal_distance += units
    if direction == "up":
        depth_distance -= units
    if direction == "down":
        depth_distance += units
position = horizontal_distance * depth_distance
print(position)
