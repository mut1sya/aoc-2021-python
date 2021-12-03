with open('input.txt') as f:
    lines = f.readlines()
bits_length = len(lines[0])

oxygen_generator_rating = 0
co2_scrubber_rating = 0
oxygen_lines = lines
for x in range(bits_length):
    new_lines_1 = []
    new_lines_0 = []
    if len(oxygen_lines) > 1:
        counter_1=0
        counter_0=0
        for line in oxygen_lines:
            if line[x] =="1":
                counter_1 += 1
                new_lines_1.append(line)
            else:
                counter_0 += 1
                new_lines_0.append(line)
        if counter_1 > counter_0:
            oxygen_lines = new_lines_1
            new_lines_1 = []
            new_lines_0 = []
            counter = 0
        elif counter_1 == counter_0:
            oxygen_lines = new_lines_1
            new_lines_1 = []
            new_lines_0 = []
            counter = 0
        else:
            oxygen_lines = new_lines_0
            new_lines_0 = []
            new_lines_1 = []
            counter = 0
    else:
        oxygen_generator_rating = int(str(oxygen_lines[0]), 2)

co2_lines = lines
for x in range(bits_length):
    new_lines_1 = []
    new_lines_0 = []
    if len(co2_lines) > 1:
        counter_1=0
        counter_0=0
        for line in co2_lines:
            if line[x] =="1":
                counter_1 += 1
                new_lines_1.append(line)
            else:
                counter_0 += 1
                new_lines_0.append(line)
        if counter_1 < counter_0:
            co2_lines = new_lines_1
            new_lines_1 = []
            new_lines_0 = []
            counter = 0
        elif counter_1 == counter_0:
            co2_lines = new_lines_0
            new_lines_1 = []
            new_lines_0 = []
            counter = 0
        else:
            co2_lines = new_lines_0
            new_lines_0 = []
            new_lines_1 = []
            counter = 0
    else:
        co2_scrubber_rating = int(str(co2_lines[0]), 2)

print(oxygen_generator_rating*co2_scrubber_rating)



