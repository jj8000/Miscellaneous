from random import randint


fields = [' ' for i in range(9)]
f = fields


def draw():
    print(f" {fields[0]} | {fields[1]} | {fields[2]}\n"
          f" {fields[3]} | {fields[4]} | {fields[5]}\n"
          f" {fields[6]} | {fields[7]} | {fields[8]}\n")


def computer_move():
    while True:
        chosen_field = randint(0, 8)
        if fields[chosen_field] == ' ':
            break
    fields[chosen_field] = 'O'


def victory():
    rows = [f[0:3], f[3:6], f[6:9]]
    columns = [f[0:7:3], f[1:8:3], f[2:9:3]]
    diagonals = [f[0:9:4], f[2:7:2]]
    lines = rows + columns + diagonals
    if ['X', 'X', 'X'] in lines:
        return True
    if ['O', 'O', 'O'] in lines:
        return False
    else:
        return None

print(" 1 | 2 | 3\n"
        " 4 | 5 | 6\n"
        " 7 | 8 | 9\n")
while True:
    while True:
        try:
            move = int(input("Podaj pole (1 - 9): "))
        except ValueError:
            print("Nieprawidłowe polecenie")
            continue
        if move not in [_ for _ in range(10)]:
            print("Nieprawidłowe polecenie")
            continue
        if fields[int(move) - 1] != ' ':
            print("Pole zajęte")
        else:
            break
    fields[int(move) - 1] = 'X'
    draw()
    if ' ' not in fields:
        print("Remis!")
        break
    if victory() == True:
        print("Wygrałeś!")
        break
    print("Ruch komputera:")
    computer_move()
    draw()
    if victory() == False:
        print("Przegrałeś!")
        break
