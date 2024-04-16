import sys,os

l,h = os.get_terminal_size()
def write(text='',x=int,y=int,color=[],pixel=False,flush=True):
    extra=''
    for c in color:
       extra+=c 
    if not x==int:
        if pixel: x=x*2
        sys.stdout.write(f'\033[{y};{x}f')
    sys.stdout.write(extra+text)
    if flush: sys.stdout.flush()

def flush():
    sys.stdout.flush()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class Color:
    default = '\033[0m'
    darkend = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    blinky = '\033[5m'
    selcted = '\033[7m'
    invisible = '\033[8m'
    strikethru = '\033[9m'
    hidecursor = '\033[?25l'
    showcursor = '\033[?25h'
    black = lambda:None
    black.fg = '\033[30m'
    black.bg =  '\033[30m'
    red = lambda:None
    red.fg = '\033[31m'
    red.bg = '\033[41m'
    green = lambda:None
    green.fg = '\033[32m'
    green.bg = '\033[42m'
    yellow = lambda:None
    yellow.fg = '\033[33m'
    yellow.bg = '\033[43m'
    blue = lambda:None
    blue.fg = '\033[34m'
    blue.bg = '\033[44m'
    magenta = lambda:None
    magenta.fg = '\033[35m'
    magenta.bg = '\033[45m'
    cyan = lambda:None
    cyan.fg = '\033[36m'
    cyan.bg = '\033[46m'
    light_gray = lambda:None
    light_gray.fg ='\033[37m'
    light_gray.bg = '\033[47m'
    gray = lambda:None
    gray.fg = '\033[90m'
    gray.bg = '\033[100m'
    light_red = lambda:None
    light_red.fg = '\033[91m'
    light_red.bg = '\033[101m'
    light_green = lambda:None
    light_green.fg = '\033[92m'
    light_green.bg = '\033[102m'
    light_yellow = lambda:None
    light_yellow.fg = '\033[93m'
    light_yellow.bg = '\033[103m'
    light_blue = lambda:None
    light_blue.fg = '\033[94m'
    light_blue.bg = '\033[104m'
    light_magenta = lambda:None
    light_magenta.fg = '\033[95m'
    light_magenta.bg = '\033[105m'
    light_cyan = lambda:None
    light_cyan.fg = '\033[96m'
    light_cyan.bg = '\033[106m'
    white = lambda:None
    white.fg = '\033[97m'
    white.bg = '\033[107m'
    code = {'0':black,'1':blue,'2':green,'3':cyan,'4':red,'5':magenta,'6':yellow,'7':light_gray,'8':gray,'9':light_blue,'a':light_green,'b':light_cyan,'c':light_red,'d':light_magenta,'e':light_yellow,'f':white}

color = Color