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
while trong():
    #nguoi_choi
    nguoi=int(input('Hãy chọn 1 ô trong [0...8]:'))
    if luoi[nguoi]=='X' or luoi[nguoi]=='O':
        print('ô đã bị chọn')
    else:
        luoi[nguoi]='X'

    #may
    may=randint(0,8)
    if luoi[may]=='O' or luoi[may]=='X':
        pass
    else:
        luoi[may]='O'
    inluoi()