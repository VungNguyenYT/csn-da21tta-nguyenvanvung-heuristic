# Ý TƯỞNG
#
# - Trò chơi tic tac toe(cờ caro)
#   + Dùng if else để kiểm tra các ô, nếu đã chọn thì bỏ qua
#
# - Cho máy tìm đường đi bằng thuật toán Heuristic
#   + Duyệt qua các dòng ngang, các cột dọc và các đường chéo  
#   + Nếu có 2 ô liên tiếp của máy và một ô trống kế bên thì chọn vào ô đó để chiến thắng
#   + Nếu có 2 ô liên tiếp và một ô trống nằm trên đường thẳng(đối với đường chéo) thì chọn vào ô đó để chiến thắng
#
#****************************************************
#******************* IN RA BÀN CỜ *******************
from operator import truediv
from random import randint

# Tạo lưới
luoi = [' '] * 9  #Sử dụng ký tự trắng để thể hiện ô trống
win = ''

#In ra bàn cờ(lưới 3x3)
def inluoi():
    for i in range(0, 9, 3):
        print(luoi[i], '|', luoi[i + 1], '|', luoi[i + 2])
        if i < 6:
            print('---------')

inluoi()


#******************* GAMEPLAY *******************
#kiểm tra vị trí có còn trống không
def trong():
    for i in range(9):
        if luoi[i] == ' ':
            return True
    return False

#Kiểm tra dòng
def ktra_dong(chon,x1,x2,x3):
    if luoi[x1]==chon and luoi[x2]==chon and luoi[x3]==chon:
        return True
    return False

def Ktra_all(chon):
    #Kiểm tra dòng ngang
    if ktra_dong(chon,0,1,2)==True: #Kiểm tra dòng 1
        return True
    if ktra_dong(chon,3,4,5)==True: #Kiểm tra dòng 2
        return True
    if ktra_dong(chon,6,7,8)==True: #Kiểm tra dòng 3
        return True
    
    #kiểm tra hàng dọc
    if ktra_dong(chon,0,3,6)==True: #Kiểm tra cột 1
        return True
    if ktra_dong(chon,1,4,7)==True: #Kiểm tra cột 2
        return True
    if ktra_dong(chon,2,5,8)==True: #Kiểm tra cột 3
        return True
    
    #kiểm tra 2 đường chéo
    if ktra_dong(chon,0,4,8)==True: #Kiểm tra đường chéo trái
        return True
    if ktra_dong(chon,2,4,6)==True: #Kiểm tra đường chéo phải
        return True
    return False

#Thuật toán heuristic duyệt qua lần lượt các ô để tìm cơ hội thắng
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

    #Nếu không chọn được thì máy đi ngẫu nhiên
    empty_cells = [i for i in range(9) if luoi[i] == ' ']
    return randint(0, len(empty_cells) - 1)

while trong():
    #Người chơi
    nguoi = int(input('Hãy chọn 1 ô trong [0...8]:'))
    if luoi[nguoi] == 'X' or luoi[nguoi] == 'O':
        print('Ô đã bị chọn')
    else:
        luoi[nguoi] = 'X'
    inluoi()

    #In ra người chơi thắng
    if Ktra_all('X'):
        win = 'Bạn'
        break

    #Kiểm tra xem còn ô trống không, nếu không còn trò chơi kết thúc
    if not trong():
        print('Hòa')
        break

    
    #Máy
    may = heuristic_move()
    if luoi[may]=='X' or luoi[may]=='O':
        pass
    else:
        luoi[may]='O'
    inluoi()

    #In ra máy thắng
    if Ktra_all('O'):
        win = 'Máy'
        break

#kiểm tra game hòa, in ra người chiến thắng
if win == '':
    print('Hòa')
else:
    print(win, 'Thắng')
