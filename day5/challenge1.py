def read_and_parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
    input_data = []
    for line in lines:
        line_coordinates = line.rstrip('\n').split(' -> ')
        coordinate = {
            "start": line_coordinates[0].split(','),
            "end": line_coordinates[1].split(',')
        }
        input_data.append(coordinate)
    return input_data

def setup_matrix(height, width):
    matrix = []
    for x in range(height):
        matrix.append([])
        for y in range(width):
            matrix[x].append(0)
    return matrix
            
def determine_type_of_line(line):
    if line['start'][0] == line['end'][0]:
        return 'vertical'
    elif line['start'][1] == line['end'][1]:
        return 'horizonatal'
    else:
        return "other"

def plot_horizontal_line(line, matrix):
    line_length = int(line['end'][0]) -  int(line['start'][0]) 
    if line_length >0:
        direction = "forward"
    else:
        direction = "backward"
    line_length = abs(line_length)+1 #include the end point
    
    update_row = int(line['start'][1])
    update_forward_point = int(line['start'][0])
    update_backward_point = int(line['end'][0])
    for x in range(line_length):
        if direction == "forward":
            matrix[update_row][update_forward_point] += 1
            update_forward_point += 1
        elif direction == 'backward':
            matrix[update_row][update_backward_point] += 1
            update_backward_point +=1
        else:
            pass


def plot_vertical_line(line, matrix):
    line_length = int(line['end'][1]) -  int(line['start'][1]) 
    if line_length >0:
        direction = "forward"
    else:
        direction = "backward"
    
    line_length = abs(line_length)+1 #include the end point
    update_column = int(line['start'][0])
    update_forward_point = int(line['start'][1])
    update_backward_point = int(line['end'][1])
    for x in range(line_length):
        if direction == "forward":
            matrix[update_forward_point][update_column] += 1
            update_forward_point += 1
        elif direction == 'backward':
            matrix[update_backward_point][update_column] += 1
            update_backward_point +=1
        else:
            pass

def compute_score(matrix):
    sum = 0
    for row in matrix:
        for point in row:
            if point >= 2:
                sum += 1
    return sum



input_data = read_and_parse_input()
matrix = setup_matrix(1000, 1000)

for line in input_data:
    line_type = determine_type_of_line(line)
    if line_type == "vertical":
        plot_vertical_line(line, matrix)
    elif line_type =="horizonatal":
        plot_horizontal_line(line, matrix)

score = compute_score(matrix)
print(score)

