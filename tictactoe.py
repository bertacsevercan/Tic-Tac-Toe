

from string import digits

cells = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")

m = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
coodinates = ["1", "2", "3"]
turn = 0
x_count_ = 0
o_count_ = 0
x_count = 0
o_count = 0
sign = ""
condition = True

def check(sign):
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2] == sign \
        or m[0][i] == m[1][i] == m[2][i] == sign \
        or m[0][0] == m[1][1] == m[2][2] == sign \
        or m[0][2] == m[1][1] == m[2][0] == sign:
            return True
def imp_check():
    global x_count,o_count
    for i in range(3):
        for j  in range(3):
            if m[i][j] == "X":
                x_count +=1
            if m[i][j] == "O":
                o_count +=1
            if abs(x_count - o_count) != 0 or abs(x_count - o_count) != 1:
                return True
def imp_check2():
    global x_count_,o_count_
    for i in range(3):
        if check("X"):
            x_count_ +=1
        if check("O"):
            o_count_ +=1
        if x_count_ and o_count_ >=1:
            return True
def big_check():
        global condition
        if check("X"):
            print("X wins")
            condition = False
        elif check("O"):
            print("O wins")
            condition = False
        elif "_" not in m[0] and "_" not in m[1] and "_" not in m[2]:
            print("Draw")
            condition = False
def print_board():
      print(f"""---------
| {m[0][0]} {m[0][1]} {m[0][2]} |
| {m[1][0]} {m[1][1]} {m[1][2]} |
| {m[2][0]} {m[2][1]} {m[2][2]} |
---------""")

while condition:
    user_move = input("Enter the coordinates: ").split()
    if turn % 2 == 0:
        sign = "X"

        if m[2][0] == "_" and user_move[0] == "1" and user_move[1] == "1":
            m[2][0] = sign
            print_board()
            big_check()

        elif m[1][0] == "_" and user_move[0] == "1" and user_move[1] == "2":
            m[1][0] = sign
            print_board()
            big_check()


        elif m[0][0] == "_" and user_move[0] == "1" and user_move[1] == "3":
            m[0][0] = sign
            print_board()
            big_check()

        elif m[2][1] == "_" and user_move[0] == "2" and user_move[1] == "1":
            m[2][1] = sign
            print_board()
            big_check()


        elif m[1][1] == "_" and user_move[0] == "2" and user_move[1] == "2":
            m[1][1] = sign
            print_board()
            big_check()


        elif m[0][1] == "_" and user_move[0] == "2" and user_move[1] == "3":
            m[0][1] = sign
            print_board()
            big_check()


        elif m[2][2] == "_" and user_move[0] == "3" and user_move[1] == "1":
            m[2][2] = sign
            print_board()
            big_check()


        elif m[1][2] == "_" and user_move[0] == "3" and user_move[1] == "2":
            m[1][2] = sign
            print_board()
            big_check()


        elif m[0][2] == "_" and user_move[0] == "3" and user_move[1] == "3":
            m[0][2] = sign
            print_board()
            big_check()


        elif str(user_move[0]) and str(user_move[1]) not in digits:
            print("You should enter numbers!")
            continue

        elif user_move[0] and user_move[1] not in coodinates:
            print("Coordinates should be from 1 to 3!")
            continue

        else:
            print("This cell is occupied! Choose another one!")
            continue
    else:
        sign = "O"

        if m[2][0] == "_" and user_move[0] == "1" and user_move[1] == "1":
            m[2][0] = sign
            print_board()
            big_check()

        elif m[1][0] == "_" and user_move[0] == "1" and user_move[1] == "2":
            m[1][0] = sign
            print_board()
            big_check()


        elif m[0][0] == "_" and user_move[0] == "1" and user_move[1] == "3":
            m[0][0] = sign
            print_board()
            big_check()

        elif m[2][1] == "_" and user_move[0] == "2" and user_move[1] == "1":
            m[2][1] = sign
            print_board()
            big_check()


        elif m[1][1] == "_" and user_move[0] == "2" and user_move[1] == "2":
            m[1][1] = sign
            print_board()
            big_check()


        elif m[0][1] == "_" and user_move[0] == "2" and user_move[1] == "3":
            m[0][1] = sign
            print_board()
            big_check()


        elif m[2][2] == "_" and user_move[0] == "3" and user_move[1] == "1":
            m[2][2] = sign
            print_board()
            big_check()


        elif m[1][2] == "_" and user_move[0] == "3" and user_move[1] == "2":
            m[1][2] = sign
            print_board()
            big_check()


        elif m[0][2] == "_" and user_move[0] == "3" and user_move[1] == "3":
            m[0][2] = sign
            print_board()
            big_check()

        elif str(user_move[0]) and str(user_move[1]) not in digits:
            print("You should enter numbers!")
            continue

        elif user_move[0] and user_move[1] not in coodinates:
            print("Coordinates should be from 1 to 3!")
            continue


        else:
            print("This cell is occupied! Choose another one!")
            continue

    turn += 1





