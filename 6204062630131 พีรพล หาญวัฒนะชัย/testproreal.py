from tkinter import*
import random
from tkinter import messagebox
from csv import*

def ran(p1s): 
         if random.random() <= (1/8):
                  p2s = "44"
         elif (1/8) < random.random() <= (2/8):
                  p2s = "PY"
         elif (2/8) < random.random() <= (3/8):
                  p2s = "PW"
         elif (3/8) < random.random() <= (4/8):
                  p2s = "TT"
         elif (4/8) < random.random() <= (5/8):
                  p2s = "RT"
         elif (5/8) < random.random() <= (6/8):
                  p2s = "CH"
         elif (6/8) < random.random() <= (7/8):
                  p2s = "SR"
         else:
                  p2s = "PN"
                  

#rule
         
         global x2
         global total_m
         if p2s == p1s:
                  result = "Draw(Nice Try)"
                  total_m +=0
                  
                  
                  
    
         elif(p2s == 'PY' and p1s == '44') or (p2s == 'PW' and p1s == '44') or (p2s == 'TT' and p1s == '44') or (p2s == 'RT' and p1s == '44')\
                     or (p2s == 'CH' and p1s == '44') or (p2s == 'SR' and p1s == '44') or (p2s == 'PN' and p1s == '44') or (p2s == 'PW' and p1s == 'PY')\
                     or (p2s == 'RT' and p1s == 'PY') or (p2s == 'CH' and p1s == 'PY') or(p2s == 'PN' and p1s == 'PY') or (p2s == 'RT' and p1s == 'PW')\
                     or (p2s == 'CH' and p1s == 'PW')or (p2s == 'PN' and p1s == 'PW')or (p2s == 'PY' and p1s == 'TT') or (p2s == 'PW' and p1s == 'TT')\
                     or (p2s == 'PN' and p1s == 'TT') or (p2s == 'TT' and p1s == 'RT')or (p2s == 'CH' and p1s == 'RT')or (p2s == 'SR' and p1s == 'RT')\
                     or (p2s == 'PN' and p1s == 'RT') or (p2s == 'TT' and p1s == 'CH')or (p2s == 'SR' and p1s == 'CH') or (p2s == 'PN' and p1s == 'CH')\
                     or (p2s == 'PY' and p1s == 'SR')or (p2s == 'PW' and p1s == 'SE')or (p2s == 'TT' and p1s == 'SR') or (p2s == 'PN' and p1s == 'SR'):
                  result = "You won(Well Play)"
                  total_m += 30
         else:
                  result = "You noob(EZ DOG)"
                  total_m -= 10
         x2.set(total_m)



         global screen
         screen.config(text="Computer choose: " + p2s + "\n" + result,background='pink')
                           

#command btn jaaaaaa
def x44():
         ran("44")
         

def xpy():
         ran("PY")

def xpw():
         ran("PW")

def xtt():
         ran("TT")

def xrt():
         ran("RT")

def xch():
         ran("CH")

def xsr():
         ran("SR")

def xpn():
         ran("PN")




#tk kaaaaaaaaaaa
f = Tk()
f.minsize(1200,800)
f.maxsize(1200,800)
f.title("ไพ่เป่ายิ้งฉุบ")
f.configure(background='pink')   



##----------------------------
x1=IntVar()
x2=StringVar()
total_m=1000


##photo
p44 = PhotoImage(file="44.png")
ppy = PhotoImage(file="PY.png")
ppw = PhotoImage(file="PW.png")
ptt = PhotoImage(file="TT.png")
prt = PhotoImage(file="RT.png")
pch = PhotoImage(file="CH.png")
psr = PhotoImage(file="SR.png")
ppn = PhotoImage(file="PN.png")


##btn
l1 = Label(f)
l1.place(x=10,y=600)
b1 = Button(l1, image=p44,borderwidth=0,command=x44)
b1.pack(side=LEFT,padx=15)
b2 = Button(l1, image=ppy,borderwidth=0,command=xpy)
b2.pack(side=LEFT,padx=15)
b3 = Button(l1, image=ppw,borderwidth=0,command=xpw)
b3.pack(side=LEFT,padx=15)
b4 = Button(l1, image=ptt,borderwidth=0,command=xtt)
b4.pack(side=LEFT,padx=15)
b5 = Button(l1, image=prt,borderwidth=0,command=xrt)
b5.pack(side=LEFT,padx=15)
b6 = Button(l1, image=pch,borderwidth=0,command=xch)
b6.pack(side=LEFT,padx=15)
b7 = Button(l1, image=psr,borderwidth=0,command=xsr)
b7.pack(side=LEFT,padx=15)
b8 = Button(l1, image=ppn,borderwidth=0,command=xpn)
b8.pack(side=LEFT,padx=15)

## screen
screen = Label(f,fg = "skyblue", text="Choose your card",font="consolas 25",background='pink')
screen.place(x=10,y=100)



##entry money naja
##le1= Label(f,text="เงินเดิมพัน",font="consolas 25")
##le1.place(x=50,y=200)
##e1=Entry(f,textvariable=x1,font="consolas 25")
##e1.place(x=50,y=250)

##money show
m1 = Label(f,text="เงินคงเหลือปัจจุบัน",font="consolas 25",background='pink')
m1.place(x=900,y=100)
l3 = Label(f, textvariable=x2, width=20, bg="skyblue",font="consolas 25")
l3.place(x=800,y=150)



##tutorrail
def how():
         global bp1
         messagebox.showinfo("อ่านด้วยไอพวกโง่","1)การ์ด44ชนะทุกใบเพราะแม่งโกง"+"\n"+"2)การ์ดPYชนะPW,RT,CH,PN"+"\n"+"3)การ์ดPWชนะRT,CH,PN"+"\n"+"4)การ์ดTTชนะPY,PW,PN"+"\n"+"5)การ์ดRTชนะTT,CH,SR,PN"+"\n"+"6)การ์ดCHชนะTT,SR,PN"+"\n"+"7)การ์ดSRชนะPY,PW,PW,TT,PN"+"\n"+"8)การ์ดPNไม่ชนะใครเลยเพราะแม่งกาก")

bp1 = Button(f,text="Rule",command=how)
bp1.place(x=1100,y=250)

def tutor():
         global bp2
         messagebox.showinfo("อ่านด้วยไอพวกโง่","มีเงินให้จำนวน 1000 "+"\n"+"ถ้าชนะจำนวนเงิน+30 "+"\n"+"ถ้าเเสมอจะไม่บวกจำนวนเงิน "+"\n"+"ถ้าเเพ้จำนวนเงินจะถูก -10 ")

bp2 = Button(f,text="tutorial",command=tutor)
bp2.place(x=1100,y=300)
         


## Save KUB
def sv():
         with open('save_m.csv','a') as pez:
                  w = writer(pez,lineterminator='\n')
                  w.writerow( [x2.get()] )

bs = Button(f,text="SAVE",command=sv)
bs.place(x=1100,y=350)

## load jaaaaaaa
def load():
         with open('save_m.csv','r') as ppl:
                  gg=reader(ppl)
                  ez=list(gg)
         for column in ez:
                  Label(f,text='{}'.format(column[0]),bg='skyblue',font="consolas 25", width=20).place(x=1,y=450)

bzl = Button(f,text="LOAD",command=load)
bzl.place(x=1100,y=400)

## money show load
m2 = Label(f,text="เงินคงเหลือล่าสุด(LOAD)",font="consolas 25", width=20,background='pink')
m2.place(x=1,y=400)



f.mainloop()


         




                           

         
                   
         
