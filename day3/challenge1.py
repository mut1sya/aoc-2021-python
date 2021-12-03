with open('input.txt') as f:
    lines = f.readlines()
list_length = len(lines)
bit_results = []
for bit in lines[0].rstrip("\n"):
    bit_results.append(0)

for line in lines:
    for x in range(len(line)):
        if line[x] == "1":
            bit_results[x] += 1

gamma_rate_list = []
epsilon_rate_list = []
for x in bit_results:
    if x >= list_length/2:
        gamma_rate_list.append("1")
        epsilon_rate_list.append("0")
    else:
        gamma_rate_list.append("0")
        epsilon_rate_list.append("1")

gamma_rate = int("".join(gamma_rate_list), 2)
epsilon_rate = int("".join(epsilon_rate_list), 2)

print(gamma_rate)

print(epsilon_rate)

result = gamma_rate * epsilon_rate
print(result)
# print(bit_results)
