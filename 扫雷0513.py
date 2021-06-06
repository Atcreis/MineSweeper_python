import random
import copy
import turtle as t
import tkinter
import tkinter.messagebox

def shengchenlei(a):
    #生成储存数量为a的雷的序列
    bomblist=[]
    for i in range(6):
        alist=[]
        for j in range(6):
            alist.append(0)
        bomblist.append(alist)
    i=1
    while i<=a:
        xx=random.randint(0,5)
        yy=random.randint(0,5)
        if bomblist[xx][yy]==-1:
            continue
        else:
            bomblist[xx][yy]=-1
            i+=1
    return bomblist

def quanxulie(bomblist):
    q=copy.deepcopy(bomblist)
    q.insert(0,[0]*6)
    q.append([0]*6)
    for m in range(8):
        q[m].insert(0,0)
        q[m].append(0)
    for i in range(1,7):
        for j in range(1,7):
            if q[i][j]==-1:
                continue
            else:
                for k in (i-1,i,i+1):
                    for l in (j-1,j,j+1):
                        bomblist[i-1][j-1]-=q[k][l]
                bomblist[i-1][j-1]+=q[i][j]
    return bomblist

def w():
    w=copy.deepcopy(bomblist)
    w.insert(0,[9]*6)
    w.append([9]*6)
    for m in range(8):
        w[m].insert(0,9)
        w[m].append(9)
    return w

def xswlxulie():
    xs=[]
    for i in range(6):
        dlist=[]
        for j in range(6):
            dlist.append(0)
        xs.append(dlist)
    return xs    

def xswl(x,y,bomblist):
    if xs[x][y]<=1:
        tuse(x,y,'green')
        for i in [x,x+1,x+2]:
            for j in [y,y+1,y+2]:
                if 1<=i and i<=6 and 1<=j and j<=6:
                    if w[i][j]==0:
                        tuse(i-1,j-1,'green')
                        xs[i-1][j-1]+=1
                        xswl(i-1,j-1,bomblist)
                    elif w[i][j]!=9:
                        tuse(i-1,j-1,'green')
                        xianshuzi(i-1,j-1,bomblist)
                    else:
                        tuse(x,y,'green')
                else:
                    tuse(x,y,'green')
        xs[x][y]+=1
    
def huagezi(x):
    #暂时先画6*6格子，没用变量x
    t.pencolor('black')
    t.hideturtle()
    t.tracer(False)
    t.speed(10)
    for k in range(6):
        t.penup()
        t.goto(-150,-150+50*k)
        t.pendown()
        for j in range (6):
            for i in range(4):
                t.forward(50)
                t.left(90)
            t.forward(50)
    t.update()

def shuzixulie():
    shuzilie=[]
    for i in range(6):
        clist=[]
        for j in range(6):
            clist.append(0)
        shuzilie.append(clist)
    return shuzilie

def xianshuzi(a,b,bomblist):
    #给序列索引，填充相应数字
    if shuzilie[a][b]==0:
        sy=100-50*a+20
        sx=50*b-150+25
        t.hideturtle()
        t.tracer(False)
        t.speed(10)
        t.penup()
        t.goto(sx,sy)
        t.pendown()
        t.write(bomblist[a][b])
        t.update()
        shuzilie[a][b]=1

def tusexulie():
    tuselie=[]
    for i in range(6):
        blist=[]
        for j in range(6):
            blist.append(0)
        tuselie.append(blist)
    return tuselie
    
def tuse(x,y,fcolor):
    #输入序列索引、颜色，对对应格子涂色
    if tuselie[x][y]==0:
        ty=100-50*x
        tx=50*y-150
        t.fillcolor(fcolor)
        t.hideturtle()
        t.tracer(False)
        t.speed(10)
        t.penup()
        t.goto(tx,ty)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.update()
        tuselie[x][y]=1

def dingwei(x,y):
    #输入坐标，返回序列索引
    x/=50
    y/=50
    if x>=0:
        yyy=int(x)+3
    else:
        yyy=int(x)+2
    if y>=0:
        xxx=2-int(y)
    else:
        xxx=3-int(y)
    return xxx,yyy

def saoleixulie():
    now=copy.deepcopy(bomblist)
    return now

def tuhuangse(x,y):
    ty=100-50*x
    tx=50*y-150
    if tuselie[x][y]==0 and now[x][y]<9:
        t.fillcolor('yellow')
        t.hideturtle()
        t.tracer(False)
        t.speed(10)
        t.penup()
        t.goto(tx,ty)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.update()
        if now[x][y]==-1:
            now[x][y]=10
        else:
            now[x][y]=11
    elif tuselie[x][y]==0 and now[x][y]>9:
        t.fillcolor('white')
        t.hideturtle()
        t.tracer(False)
        t.speed(10)
        t.penup()
        t.goto(tx,ty)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.update()
        now[x][y]=bomblist[x][y]
    #赢得游戏判定1
    else:
        pass
    c=0
    for a in range(6):
        for b in range(6):
            if now[a][b]==10:
                c+=1
            elif now[a][b]==11:
                    c-=1
            else:
                pass
    if c==5:                             #如果c等于雷的数量
        tkinter.messagebox.showinfo('提示','you win')
        t.bye()

def leftclick(x,y):
    if -150<=x<=150 and -150<=y<=150:
        xx=dingwei(x,y)[0]
        yy=dingwei(x,y)[1]
        if bomblist[xx][yy]==-1:
            tuse(xx,yy,'red')
            tkinter.messagebox.showinfo('提示','you lose')
            t.bye()
        else:
            if bomblist[xx][yy]!=0:
                tuse(xx,yy,'green')
                xianshuzi(xx,yy,bomblist)
                #赢得游戏判定2
                d=0
                for i in range(6):
                    for j in range(6):
                        if tuselie[i][j]==0:
                            d+=1
                if d==5:                            #如果d等于雷的数量
                    tkinter.messagebox.showinfo('提示','you win')
                    t.bye()
                else:
                    t.mainloop()
            else:
                xswl(xx,yy,bomblist)
                t.mainloop()

def rightclick(x,y):
    if -150<=x<=150 and -150<=y<=150:
        xx=dingwei(x,y)[0]
        yy=dingwei(x,y)[1]
        tuhuangse(xx,yy)

bomblist=shengchenlei(5)
y=quanxulie(bomblist)
tuselie=tusexulie()
shuzilie=shuzixulie()
w=w()
xs=xswlxulie()
now=saoleixulie()
#print('\n'.join(map(str,bomblist)))   #debug用
huagezi(6)
t.onscreenclick(leftclick,1)
t.onscreenclick(rightclick,3)

t.mainloop()