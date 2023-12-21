from operator import truediv
from random import randint

# Tạo lưới
luoi = [' '] * 9  # Sử dụng ký tự trắng để thể hiện ô trống
win = ''

def inluoi():
    for i in range(0, 9, 3):
        print(luoi[i], '|', luoi[i + 1], '|', luoi[i + 2])
        if i < 6:
            print('---------')

inluoi()

def trong():
    for i in range(9):
        if luoi[i] == ' ':
            return True
    return False

# Kiểm tra dòng
def ktra_dong(chon, x1, x2, x3):
    return luoi[x1] == luoi[x2] == luoi[x3] == chon

def Ktra_all(chon):
    #Kiểm tra dòng ngang
    if ktra_dong(chon,0,1,2)==True:
        return True
    if ktra_dong(chon,3,4,5)==True:
        return True
    if ktra_dong(chon,6,7,8)==True:
        return True
    
    #kiểm tra hàng dọc
    if ktra_dong(chon,0,3,6)==True:
        return True
    if ktra_dong(chon,1,4,7)==True:
        return True
    if ktra_dong(chon,2,5,8)==True:
        return True
    
    #kiểm tra 2 đường chéo
    if ktra_dong(chon,0,4,8)==True:
        return True
    if ktra_dong(chon,2,4,6)==True:
        return True
    return False

# Thuật toán heuristic
def heuristic_move():
    for i in range(0, 9, 3):
        if luoi[i] == luoi[i + 1] == 'O' and luoi[i + 2] == ' ':
            return i + 2
        elif luoi[i] == luoi[i + 2] == 'O' and luoi[i + 1] == ' ':
            return i + 1
        elif luoi[i + 1] == luoi[i + 2] == 'O' and luoi[i] == ' ':
            return i

    for i in range(3):
        if luoi[i] == luoi[i + 3] == 'O' and luoi[i + 6] == ' ':
            return i + 6
        elif luoi[i] == luoi[i + 6] == 'O' and luoi[i + 3] == ' ':
            return i + 3
        elif luoi[i + 3] == luoi[i + 6] == 'O' and luoi[i] == ' ':
            return i

    if luoi[0] == luoi[4] == 'O' and luoi[8] == ' ':
        return 8
    elif luoi[0] == luoi[8] == 'O' and luoi[4] == ' ':
        return 4
    elif luoi[4] == luoi[8] == 'O' and luoi[0] == ' ':
        return 0

    if luoi[2] == luoi[4] == 'O' and luoi[6] == ' ':
        return 6
    elif luoi[2] == luoi[6] == 'O' and luoi[4] == ' ':
        return 4
    elif luoi[4] == luoi[6] == 'O' and luoi[2] == ' ':
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

    #Người chơi thắng
    if Ktra_all('X'):
        win = 'Bạn'
        break

    #Game hòa
    if not trong():
        print('Hòa')
        break

    #Máy thắng
    may = heuristic_move()
    #luoi[may] = 'O'
    if luoi[may]=='X' or luoi[may]=='O':
        pass
    else:
        luoi[may]='O'
    inluoi()

    if Ktra_all('O'):
        win = 'Máy'
        break

if win == '':
    print('Hòa')
else:
    print(win, 'Thắng')
