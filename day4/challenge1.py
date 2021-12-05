


def set_up_board():
    global puzzle_input, boards
    with open('input.txt') as f:
        puzzle_input = f.readline().rstrip('\n').split(',')
        lines = f.readlines()
    boards = []
    for line in lines:
        tracker = -1
        if  not line.rstrip('\n'):
            tracker +=1
            boards.append([])
        else:
            line_to_array =line.rstrip('\n').split()
            line_with_markers = []
            for x in line_to_array:
                line_with_markers.append([x, False])
            boards[tracker].append(line_with_markers)
        

def play(input_values, boards):
    for input_val in input_values:
        for board in boards:
            for row in board:
                for item in row:
                    if item[0] == input_val:
                        item[1] = True
            if check_if_won_column(board):
                print(calculate_score(board, input_val))
                return
            if check_if_won_row(board):
                print(calculate_score(board, input_val))
                return


def check_if_won_row(board):
    for row in board:
        won = True
        for item in row:
            if item[1] is not True:
                won = False
                break
        if won is True:
            return True
    return False
    
def check_if_won_column(board):
    index = 0
    size = len(board)
    for i in range(size):
        won = True
        for j in range(size):
            
            if board[j][index][1] is not True:
                won = False
                break
        index+=1
        if won is True:
            return True
    return False

def calculate_score(board, input):
    sum = 0
    for row in board:
        for item in row:
            if item[1] is not True:
                sum+=int(item[0])
    return sum * int(input)
set_up_board()
play(puzzle_input, boards)