import numpy   as np
import random  as rd
import tkinter as tk
import time    as tm

nbop = 125     #number of person
chnc = 10      #chance
chnx = chnc
indt = 0

xplc = 0
yplc = 0

y = '\033[43m' #yellow
g = '\033[42m' #green
r = '\033[0m'  #reset

file = open('namelist.txt', 'r', encoding = 'UTF-8')
data = file.readlines()

rand = round(nbop*rd.random())

ln_d = len(data[rand])

wndw = tk.Tk()
wndw.title('結果')
wndw.geometry('400x600')

while(chnc >= 0):
    print('残り回数:', chnc)
    inpt = input("input:")
    
    for i in range(nbop-1):
        if(inpt in data[i]):
            indt += 1

    if(indt == 0):
        print('このライバーはいません！')

    else:
        ln_i = len(inpt)
        zero = np.zeros(ln_i)

        for i in range(ln_i):
            for j in range(ln_d-1):
                if((inpt[i] in data[rand][j]) and (i == j)):
                    zero[i] += 4

                elif((inpt[i] in data[rand][j]) and (i != j)):
                    zero[i] += 1

            if zero[i] >= 4:
                stt1 = tk.Label(text = inpt[i], bg = '#4DB56A')
                stt1.place(x = xplc, y = yplc)

                xplc += 20

            elif(zero[i] >= 1 and 4 > zero[i]):
                stt2 = tk.Label(text = inpt[i], bg = '#FFF450')
                stt2.place(x = xplc, y = yplc)

                xplc += 20

            else:
                stt3 = tk.Label(text = inpt[i])
                stt3.place(x = xplc, y = yplc)

                xplc += 20

        xplc = 0
        yplc += 40
    
        print()
        chnc -= 1
        indt = 0

    if(sum(zero) >= 4*ln_i):
        print('正解！答えは')
        print(data[rand], end = '')
        print('でした！', end ='')
        print(chnx-chnc,'回で成功')  
        break

    elif(chnc == 0):
        print('残念……答えは')
        print(data[rand], end = '')
        print('でした！')
        break

file.close()

wndw.mainloop()