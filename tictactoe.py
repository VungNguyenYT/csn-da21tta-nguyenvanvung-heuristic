from operator import truediv
from random import randint

#tạo lưới
luoi=[0,1,2,3,4,5,6,7,8]
def inluoi():
    for i in range(0,9,3):
        print(luoi[i],'|',luoi[i+1],'|',luoi[i+2])
        print('---------')

inluoi()
def trong():
    for i in range(9):
        if luoi[i]!='X' and luoi[i]!='O': #kiểm tra vị trí còn trống hay không
            return True
#gameplay
        
def ktra_dong(chon,x1,x2,x3):
    if luoi[x1]==chon and luoi[x2]==chon and luoi[x3]==chon:
        return True
    return False

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


while trong():
    #nguoi_choi
    nguoi=int(input('Hãy chọn 1 ô trong [0...8]:'))
    if luoi[nguoi]=='X' or luoi[nguoi]=='O':
        print('ô đã bị chọn')
    else:
        luoi[nguoi]='X'

    #may
    may=randint(0,8)
    if luoi[may]=='X' or luoi[may]=='O':
        pass
    else:
        luoi[may]='O'
    inluoi()
    if Ktra_all('X'):
        win='Bạn'
        break

    if Ktra_all('O'):
        win='Computer'
        break
print(win, 'Thắng')