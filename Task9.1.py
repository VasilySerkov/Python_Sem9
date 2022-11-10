def print_field(field):
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2])
    print(field[3], end=" ")
    print(field[4], end=" ")
    print(field[5])
    print(field[6], end=" ")
    print(field[7], end=" ")
    print(field[8])

def get_winner(field, player):
    win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win_combo:
        if field[i[0]] == player and field[i[1]] == player and field[i[2]] == player:
            return player

playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winner = ''
i = 0
print_field(playing_field)
while i <= 9:
    space = int(input('Введите номер клетки для хода "X": '))
    while playing_field[space-1] == 'X' or playing_field[space-1] == 'O':
        space = int(input('Клетка уже занята, повторите ввод номера клетки для хода "X": '))
    playing_field[space-1] = 'X'
    i += 1
    print_field(playing_field)
    winner = get_winner(playing_field, 'X')
    if winner == 'X':
        break
    if i == 9:
        print("Ничья")
        break
    space = int(input('Введите номер клетки для хода "O": '))
    while playing_field[space-1] == 'X' or playing_field[space-1] == 'O':
        space = int(input('Клетка уже занята, повторите ввод номера клетки для хода "O": '))
    playing_field[space-1] = 'O'
    i += 1
    print_field(playing_field)
    winner = get_winner(playing_field, 'O')
    if winner == 'O':
        break
if i != 9:
    print(f'Победил "{winner}"')