import sys,os, PIL.Image

l,h = os.get_terminal_size() 


def write(text,x,y):
    sys.stdout.write('\033[H')
    sys.stdout.write(f'\033[{x};{y}f')
    sys.stdout.write(text)
    sys.stdout.flush()

colors = dict()
colors['black'] = {"c":'\033[40m  ','rgb':(12,12,12)}
colors['red'] = {"c":'\033[41m  ','rgb':(197, 15, 31)}
colors['green'] = {"c":'\033[42m  ','rgb':(19, 161, 14)}
colors['yellow'] = {"c":'\033[43m  ','rgb':(193, 156, 0)}
colors['blue'] = {"c":'\033[44m  ','rgb':(0, 55, 218)}
colors['magenta'] = {"c":'\033[45m  ','rgb':(136, 23, 152)}
colors['cyan'] = {"c":'\033[46m  ','rgb':(58, 150, 221)}
colors['light_grey'] = {"c":'\033[47m  ','rgb':(204, 204, 204)}
colors['dark_grey'] = {"c":'\033[100m  ','rgb':(118, 118, 118)}
colors['light_red'] = {"c":'\033[101m  ','rgb':(231, 72, 86)}
colors['light_green'] = {"c":'\033[102m  ','rgb':(22, 198, 12)}
colors['light_yellow'] = {"c":'\033[103m  ','rgb':(249, 241, 165)}
colors['light_blue'] = {"c":'\033[104m  ','rgb':(59, 120, 255)}
colors['light_magenta'] = {"c":'\033[105m  ','rgb':(180, 0, 158)}
colors['light_cyan'] = {"c":'\033[106m  ','rgb':(97, 214, 214)}
colors['white'] = {"c":'\033[107m  ','rgb':(242, 242, 242)}

def closetColor(r,g,b,a=''):
    c = {}
    for color in colors:
        c[color] = abs(colors[color]['rgb'][0]-r) #r
        c[color] += abs(colors[color]['rgb'][1]-g) #g
        c[color] += abs(colors[color]['rgb'][2]-b) #
    
    min = "black"
    for color in c:
        if c[min]> c[color]:
            min = color
    return min
        
    
    
def printImg(img = PIL.Image,size=(l,h),startPos=(1,1)):
    l,h = size
    sx, sy = startPos
    img = img.resize((int(l/2),int(h)),PIL.Image.LANCZOS)
    string = ""
    for y in range(1,img.height):
        string+=f"\033[{y+sy};{sx}H"
        for x in range(1,img.width):
            color = img.getpixel((x,y))
            color = colors[closetColor(*color)]
            string+= color['c']
    print(string)



"\033[9;1HHello\033[10;1Hsup"