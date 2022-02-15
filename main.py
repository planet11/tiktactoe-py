board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
user = True  # true for x and false for o
turns = 0

def print_board(board):
    for row in board:
        for col in row:
            print(f'{col}   ', end = "")
        print()  # same as \n

# print_board(board)

def quit(user_in):
    if user_in == "q":
        print("Bye, come back again!")
        return True
    else:
        return False

def check_input(user_in):
    if not isnum(user_in):  # check if input is a number
        return False
    user_in = int(user_in)  # convert input to int

    if not num_bounds(user_in):
        return False

    return True

def isnum(user_in):
    if not user_in.isnumeric():
        print("Please enter a valid number!")
    else:
        return True

def num_bounds(user_in):
    if user_in < 1 or user_in > 9:
        print("Number is  out of bounds!")
        return False
    else:
        return True

def isTaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already used. Choose another!")
        return True
    else:
        return False

def coordinates(user_in):
     row = int(user_in / 3)
     col = user_in
     if col > 2:
         col = int(col % 3)
     return(row, col )

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user:
        return "x"
    else:
        return "o"

def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diagonal(user, board):
        return True
    else:
        return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
        else:
            return False


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_diagonal(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False

while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_in = input(f'Please enter a position from 1-9 or "q" to quit \n').lower()  # or user_input.lower()
    if quit(user_in):
        break
    if not check_input(user_in):
        print("Try again!")
        # print_board(board)
        continue
    user_in = int(user_in)-1  # to match with the array index
    coords = coordinates(user_in)

    if isTaken(coords, board):
        print("Try again!")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print_board(board)
        print(f'{active_user} wins!')
        break
    turns += 1
    if turns == 9:  # check if all the slots are taken
        print("Its a draw!")

    user = not user

