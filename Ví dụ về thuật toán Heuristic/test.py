from operator import truediv

# Tạo lưới
luoi = [0, 1, 2, 3, 4, 5, 6, 7, 8]
win = ''

def inluoi():
    for i in range(0, 9, 3):
        print(luoi[i], '|', luoi[i + 1], '|', luoi[i + 2])
        print('---------')

inluoi()

def trong():
    for i in range(9):
        if luoi[i] != 'X' and luoi[i] != 'O':
            return True

# Kiểm tra dòng
def ktra_dong(chon, x1, x2, x3):
    return luoi[x1] == luoi[x2] == luoi[x3] == chon

def Ktra_all(chon):
    # Kiểm tra dòng ngang
    for i in range(0, 9, 3):
        if ktra_dong(chon, i, i + 1, i + 2):
            return True

    # Kiểm tra hàng dọc
    for i in range(3):
        if ktra_dong(chon, i, i + 3, i + 6):
            return True

    # Kiểm tra 2 đường chéo
    if ktra_dong(chon, 0, 4, 8) or ktra_dong(chon, 2, 4, 6):
        return True

    return False

# Thuật toán heuristic
def heuristic_move():
    for i in range(0, 9, 3):
        if luoi[i] == luoi[i + 1] == 'O' and luoi[i + 2] != 'X':
            return i + 2
        elif luoi[i] == luoi[i + 2] == 'O' and luoi[i + 1] != 'X':
            return i + 1
        elif luoi[i + 1] == luoi[i + 2] == 'O' and luoi[i] != 'X':
            return i

    for i in range(3):
        if luoi[i] == luoi[i + 3] == 'O' and luoi[i + 6] != 'X':
            return i + 6
        elif luoi[i] == luoi[i + 6] == 'O' and luoi[i + 3] != 'X':
            return i + 3
        elif luoi[i + 3] == luoi[i + 6] == 'O' and luoi[i] != 'X':
            return i

    if luoi[0] == luoi[4] == 'O' and luoi[8] != 'X':
        return 8
    elif luoi[0] == luoi[8] == 'O' and luoi[4] != 'X':
        return 4
    elif luoi[4] == luoi[8] == 'O' and luoi[0] != 'X':
        return 0

    if luoi[2] == luoi[4] == 'O' and luoi[6] != 'X':
        return 6
    elif luoi[2] == luoi[6] == 'O' and luoi[4] != 'X':
        return 4
    elif luoi[4] == luoi[6] == 'O' and luoi[2] != 'X':
        return 2

    # Nếu không có nước đi chiến thắng, chọn ngẫu nhiên
    empty_cells = [i for i in range(9) if luoi[i] == ' ']
    return randint(0, len(empty_cells) - 1)

while trong():
    # Người chơi
    nguoi = int(input('Hãy chọn 1 ô trong [0...8]: '))
    if luoi[nguoi] == 'X' or luoi[nguoi] == 'O':
        print('Ô đã bị chọn')
    else:
        luoi[nguoi] = 'X'

    inluoi()

    if Ktra_all('X'):
        win = 'Bạn'
        break

    # Kiểm tra hòa
    if not trong():
        print('Hòa')
        break

    # Máy
    may = heuristic_move()
    luoi[may] = 'O'

    inluoi()

    if Ktra_all('O'):
        win = 'Máy'
        break

if win == '':
    print('Hòa')
else:
    print(win, 'Thắng')
