from color import color,write,clear,l,h, flush
import msvcrt, random, time

speed=0.1 #lower = faster

imortality = True

l,h = int(l/2),h
snake = [[round(l/2)-1,round(h/2)],[round(l/2),round(h/2)]]
snakelenght = 2
apple = [random.randrange(1,l),random.randrange(1,h)]
write(' ',color = [color.default,color.black.bg,color.white.fg])

def getkey(st=time.time()):
    out = False
    st = time.time()
    key = ''
    while time.time()<st+speed:
        while msvcrt.kbhit(): key=msvcrt.getch()
        if str(key)[2:-1] in ['w','a','s','d','e']:
            out = key
    return out
    
        #owner id998
        #num 755
        
def controll(st):
    global snake
    key = getkey(st)
    if key:
        x,y=snake[-1]
        if key == b'w':
            y-=1
        elif key == b's':
            y+=1
        elif key == b'a':
            x-=1
        elif key == b'd':
            x+=1
        elif key == b'e':
            exit()
        else:
            return
        if not [x,y] == snake[-2]:
            snake.append([x,y])
            if snake[-1] == apple: newapple()
            snake = snake[-snakelenght:]
            return
    else:
        x,y=snake[-1]
        lx,ly = snake[-2]
        snake.append([(lx-x)*-1+x,(ly-y)*-1+y])
        if snake[-1] == apple: newapple()
        snake = snake[-snakelenght:]
            

def drawscreen():
    clear()
    for s in snake:
        x,y = s
        c = snake.index(s)
        if c%2 == 1: 
            c=color.light_green.bg 
        else: 
            c=color.green.bg
            
        write('  ',x,y,[color.default,c],pixel=True,flush=False)
    write('  ',*snake[-1],[color.yellow.bg,color.black.fg],pixel=True,flush=False)
    write('  ',*apple,[color.red.bg],pixel=True,flush=False)
    write(f'Points {snakelenght-2}',0,h,color = [color.default,color.black.bg,color.red.fg,color.underline,color.hidecursor],flush=False)
    flush()


def newapple():
    global snakelenght, apple
    snakelenght+=1
    while apple in snake:
        apple = [random.randrange(1,l),random.randrange(1,h)]

def dead():
    if not imortality:
        x,y = snake[-1]
        if snake[-1] in snake[:-1] or x == 0 or y == 0 or x == l+1 or y == h+1: 
            write(f'',20,h,color = [color.default,color.black.bg,color.white.fg,color.showcursor])
            exit('You are dead')
    

while True:
    st=time.time()
    drawscreen()
    dead()
    controll(st)