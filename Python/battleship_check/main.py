from utils import *
from os import walk



game_board = []
weight_board = []
output_board = []
game_width = 0
game_height = 0



#############################################################################################################################
# This method reads in the test case file and sets the game board specifications
#############################################################################################################################
def init_board(setup_file):
    global game_board
    global weight_board
    global output_board
    global game_height
    global game_width

    # read in the files to initialize game_board
    read_file = open(setup_file, 'r')
    read_index = 0

    for line in read_file:
        line = line.rstrip()
        if read_index == 0:
            game_width = int(line)
        elif read_index == 1:
            game_height = int(line)
        else:
            game_board.append(list(line))
        read_index += 1
    
    # initialize weight_board according to game_board size
    weight_board = [[-1] * game_width for _ in range(game_height)]

    # initialize output_board to say each move is not optimal
    output_board = [['-'] * game_width for _ in range(game_height)]



#############################################################################################################################
# This method goes through the game board and assigns weights for test cases 1-7
#############################################################################################################################
def get_weight(row, col):
    global game_board
    global game_height
    global game_width

    max_weight = -1
    directional_weight = -1
    wall_piece = ['*', '?']

    # if this spot can not be chosen next
    if game_board[row][col] != '.':
        return max_weight

    # go up
    temp_row = row - 1
    while True:
        if (temp_row < 0 or game_board[temp_row][col] in wall_piece) and row - temp_row > 2:
            max_weight = max(max_weight, 4)
            break
        elif (temp_row < 0 or game_board[temp_row][col] in wall_piece) and row - temp_row == 2:
            max_weight = max(max_weight, 2)
            break
        elif (temp_row < 0 or game_board[temp_row][col] in wall_piece) and row - temp_row == 1:
            max_weight = max(max_weight, 0)
            break
        elif game_board[temp_row][col] == '.' and row - temp_row > 2:
            max_weight = max(max_weight, 3)
            break
        elif game_board[temp_row][col] == '.' and row - temp_row == 2:
            max_weight = max(max_weight, 1)
            break
        elif game_board[temp_row][col] == '.' and row - temp_row == 1:
            max_weight = max(max_weight, 0)
            break
        temp_row -= 1

    # go down
    temp_row = row + 1
    while True:
        if (temp_row >= game_height or game_board[temp_row][col] in wall_piece) and temp_row - row > 2:
            max_weight = max(max_weight, 4)
            break
        elif (temp_row >= game_height or game_board[temp_row][col] in wall_piece) and temp_row - row == 2:
            max_weight = max(max_weight, 2)
            break
        elif (temp_row >= game_height or game_board[temp_row][col] in wall_piece) and temp_row - row == 1:
            max_weight = max(max_weight, 0)
            break
        elif game_board[temp_row][col] == '.' and temp_row - row > 2:
            max_weight = max(max_weight, 3)
            break
        elif game_board[temp_row][col] == '.' and temp_row - row == 2:
            max_weight = max(max_weight, 1)
            break
        elif game_board[temp_row][col] == '.' and temp_row - row == 1:
            max_weight = max(max_weight, 0)
            break
        temp_row += 1

    # go left
    temp_col = col - 1
    while True:
        if (temp_col < 0 or game_board[row][temp_col] in wall_piece) and col - temp_col > 2:
            max_weight = max(max_weight, 4)
            break
        elif (temp_col < 0 or game_board[row][temp_col] in wall_piece) and col - temp_col == 2:
            max_weight = max(max_weight, 2)
            break
        elif (temp_col < 0 or game_board[row][temp_col] in wall_piece) and col - temp_col == 1:
            max_weight = max(max_weight, 0)
            break
        elif game_board[row][temp_col] == '.' and col - temp_col > 2:
            max_weight = max(max_weight, 3)
            break
        elif game_board[row][temp_col] == '.' and col - temp_col == 2:
            max_weight = max(max_weight, 1)
            break
        elif game_board[row][temp_col] == '.' and col - temp_col == 1:
            max_weight = max(max_weight, 0)
            break
        temp_col -= 1

    # go right
    temp_col = col + 1
    while True:
        if (temp_col >= game_width or game_board[row][temp_col] in wall_piece) and temp_col - col > 2:
            max_weight = max(max_weight, 4)
            break
        elif (temp_col >= game_width or game_board[row][temp_col] in wall_piece) and temp_col - col == 2:
            max_weight = max(max_weight, 2)
            break
        elif (temp_col >= game_width or game_board[row][temp_col] in wall_piece) and temp_col - col == 1:
            max_weight = max(max_weight, 0)
            break
        elif game_board[row][temp_col] == '.' and temp_col - col > 2:
            max_weight = max(max_weight, 3)
            break
        elif game_board[row][temp_col] == '.' and temp_col - col == 2:
            max_weight = max(max_weight, 1)
            break
        elif game_board[row][temp_col] == '.' and temp_col - col == 1:
            max_weight = max(max_weight, 0)
            break
        temp_col += 1
    
    return max_weight



#############################################################################################################################
# This method goes through the game board and assigns weights for test cases 1-7
#############################################################################################################################
def assign_weights():
    global game_board
    global weight_board
    global game_height
    global game_width

    max_weight = -1

    for row in range(game_height):
        for col in range(game_width):
            weight = get_weight(row, col)
            weight_board[row][col] = weight
            max_weight = max(max_weight, weight)
    
    return max_weight

#############################################################################################################################
# This method uses the weighted board to create an output array
#############################################################################################################################
def create_output(max_weight):
    global weight_board
    global output_board
    global game_height
    global game_width

    for row in range(game_height):
        for col in range(game_width):
            if weight_board[row][col] == max_weight:
                output_board[row][col] = '+'

#############################################################################################################################
# This method takes the final array and saves it as a string into a file in the output folder
#############################################################################################################################
def output_results(output_file):
    global output_board
    global game_height
    global game_width
    
    output_path = './battleship-output/' + output_file + '.out'
    write_file = open(output_path, 'w+')
    for row in range(game_height):
        line = ''.join(output_board[row])
        write_file.write(line + '\n')

    write_file.close()


#############################################################################################################################
# This method runs the main functionality of the program
#############################################################################################################################
def main_body(input_file, directory_name, debug):
    global game_board
    global weight_board
    global output_board
    
    input_path = directory_name + '/' + input_file
    init_board(input_path)

    if debug:
        for line in game_board:
            print(line)

    max_weight = assign_weights()

    if debug:
        for line in weight_board:
            print(line)

    create_output(max_weight)

    if debug:
        for line in output_board:
            print(line)

    output_results(input_file)




#############################################################################################################################
# This method starts off the main program
#############################################################################################################################
if __name__ == "__main__":
    directory_name = './battleship-test-cases'
    debug = False

    test_files = []
    for (dirpath, dirnames, filenames) in walk(directory_name):
        test_files.extend(filenames)
        break
    
    for test_file in test_files:
        game_board = []
        weight_board = []
        output_board = []
        game_width = 0
        game_height = 0
        main_body(test_file, directory_name, debug)