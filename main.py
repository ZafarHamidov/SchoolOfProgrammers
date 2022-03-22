field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
flag = "игра продолжается"
turn = "нолики"

def print_field(field):
    print("----------")
    print(f"| {field[0][0]}| {field[0][1]}| {field[0][2]}|")
    print("----------")
    print(f"| {field[1][0]}| {field[1][1]}| {field[1][2]}|")
    print("----------")
    print(f"| {field[2][0]}| {field[2][1]}| {field[2][2]}|")
    print("----------")

def make_move(who, field):
    y, x = map(int, input().split())
    if who == "нолики":
        print("Ходят нолики. Выберите клетку (укажите в формате: строка столбец)")
        field[y][x] = 0
    else:
        print("Ходят крестики. Выберите клетку (укажите в формате: строка столбец)")
        field[y][x] = "X"
    return field

def pick_winner(field):
# 'X'
    x1 = True
    for i in range(3):
        if field[i] == ["X", "X", "X"]:
            x1 = True
            break
        else:
            x1 = False

    x2 = True
    if (field[0][0] == "X" and field[1][0] == "X" and field[2][0] == "X") or (field[0][1] == "X" and field[1][1] == "X" and field[2][1] == "X") or (field[0][2] == "X" and field[1][2] == "X" and field[2][2] == "X"):
        x2 = True
    else:
        x2 = False

    x3 = True
    if (field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X") or (field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X"):
        x3 = True
    else:
        x3 = False
# '0'
    o1 = True
    for i in range(3):
        if field[i] == [0, 0, 0]:
            o1 = True
            break
        else:
            o1 = False

    o2 = True
    if (field[0][0] == 0 and field[1][0] == 0 and field[2][0] == 0) or (field[0][1] == 0 and field[1][1] == 0 and field[2][1] == 0) or (field[0][2] == 0 and field[1][2] == 0 and field[2][2] == 0):
        o2 = True
    else:
        o2 = False
    o3 = True
    if (field[0][0] == 0 and field[1][1] == 0 and field[2][2] == 0) or (field[0][2] == 0 and field[1][1] == 0 and field[2][0] == 0):
        o3 = True
    else:
        o3 = False
# '-'
    nig = True
    c = 0
    for i in range(3):
        if field[i].count("-") == 0:
            c += 1
    if c == 3:
        nig == False
# Result
    if x1 == True or x2 == True or x3 == True:
        return "X"
    elif o1 == True or o2 == True or o3 == True:
        return "0"
    elif nig == False:
        return "ничья"
    else:
        return "игра продолжается"
for i in range(9):
    field = make_move(turn, field)
    if turn == "нолики":
        turn = "крестики"
    else:
        turn = "нолики"
    print_field(field)

    flag = pick_winner(field)
    if flag == "X":
        print("Победа крестиков!")
        break
    elif flag == "0":
        print("Победа ноликов!")
        break
    elif flag == "ничья":
        print("Ничья!")
        break

# 100 строк Юху!