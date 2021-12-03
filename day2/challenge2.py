with open('input.txt') as f:
    lines = f.readlines()
horizontal_distance = 0
depth_distance = 0
aim = 0
for line in lines:
    direction = line.split()[0]
    units = int(line.split()[1])
    if direction == "forward":
        horizontal_distance += units
        depth_distance = depth_distance + (aim * units)
    if direction == "up":
        aim -= units
    if direction == "down":
        aim += units
position = horizontal_distance * depth_distance
print(position)
