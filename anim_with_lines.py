# this wolf by                  __
#     Blazej Kozlowski        .d$$b
#                           .' TO$;\
# Program by               /  : TP._;
#    Anthony Cosaque      / _.;  :Tb|
#                        /   /   ;j$j
#                    _.-"       d$$$$
#                  .' ..       d$$$$;
#                 /  /P'      d$$$$P. |\
#                /   "      .d$$$P' |\^"l
#              .'           `T$P^"""""  :
#          ._.'      _.'                ;
#       `-.-".-'-' ._.       _.-"    .-"
#     `.-" _____  ._              .-"
#    -(.g$$$$$$$b.              .'
#      ""^^T$$$P^)            .(:
#        _/  -"  /.'         /:/;
#     ._.'-'`-'  ")/         /;/;
#  `-.-"..--""   " /         /  ;
# .-" ..--""        -'          :
# ..--""--.-"         (\      .-(\
#   ..--""              `-\(\/;`
#     _.                      :
#                             ;`-
#                            :\
from vendetta import *

import random

class MainWindow:

    HEIGHT = 620

    def __init__(self):
    
        self.frame = tkinter.Frame(
            V.tk,
            background = 'yellow')
        self.frame.grid(column = V.tk.grid_size()[0] + 1, row = 0)
        
        self.canvas = tkinter.Canvas(
            self.frame,
            background = 'black',
            width = 400,
            height = MainWindow.HEIGHT)
        self.canvas.grid(row = 0, column = 0)
        
        self.text_lines_counted = V.canvas.create_text( # <------- in V.canvas
            10, 10, justify = 'left', anchor = 'nw',
            text = 0, fill = 'cyan')

        self.canvas.update()

    def main(self):
        asyncio.run(self.drawing())
        self.canvas.update()
        
    async def asy_main(self):
        await self.drawing()
        self.canvas.update()
        await asyncio.sleep(0)
    
    async def drawing(self):
        
        l = [] ; some_x = {random.randrange(2, 40, 2) for _ in range(10)}
        for x in some_x:
            l += [self.canvas.create_line(
                x * 10, MainWindow.HEIGHT - 10,
                x * 10, MainWindow.HEIGHT - 20, fill = 'cyan')]
                
        await asyncio.sleep(0)
        
        l_del = []
        for y in range(MainWindow.HEIGHT - 30, 0, -10):
            same_line = []
            for line in l.copy():
            
                coord = self.canvas.coords(line)
                if coord[-2] == coord[-4]: # at lats one line straigth
                    r = random.randrange(50)
                    
                    if  r in [4, 3]:
                        if r == 4:  x = coord[-2] + 10
                        else:
                            x = coord[-2] - 10
                            for i in same_line:
                                if x < i[0]:
                                    x = coord[-2]
                    elif len(l) < 12 and r in [1, 2]:
                        pos = coord[:] + [coord[-2], y]
                        l.append(self.canvas.create_line(
                            pos, fill = 'white'))
                        x = coord[-2]
                        x += 10 if r == 1 else - 10
                    else: x = coord[-2]
                    if x <= 0 or x >= 400 : x = coord[-2]
                else: x = coord[-2]
                
                self.canvas.coords(line, coord + [x, y])
                if (x, y) in same_line:
                    l.remove(line)
                    l_del += [line]
                else:
                    same_line.append((x, y))
            # V.tk.update() ; time.sleep(0.04)
            await asyncio.sleep(0)        
        # V.tk.update() ; time.sleep(0.017)
        for line in l + l_del:
            self.canvas.itemconfig(line, fill='blue')
        for line in range(l[-1] - 200, l[-1] - 300):
            options = self.canvas.itemconfig(line)
            if not options:
                continue
            elif options['fill'][4] == 'magenta':
                continue
            self.canvas.itemconfig(line, fill='magenta')
            coord = self.canvas.coords(line)
            new_c = [j + (1 if not i % 2 else 0) for i, j in enumerate(coord)]
            self.canvas.coords(line, new_c)
        for line in range(l[-1] - 350, l[-1] - 300):
            options = self.canvas.itemconfig(line)
            if not options:
                continue
            elif options['fill'][4] == 'grey':
                continue
            self.canvas.itemconfig(line, fill='grey')
            coord = self.canvas.coords(line)
            new_c = [j + (1 if not i % 2 else 0) for i, j in enumerate(coord)]
            self.canvas.coords(line, new_c)
        for line in range(l[-1] - 350):
           self.canvas.delete(line)
        # print(self.canvas.find('all')[-1])
        V.canvas.itemconfig(
            self.text_lines_counted, text = self.canvas.find('all')[-1])
        
        
if __name__ == '__main__' :

    instance = MainWindow()
    while 1:
        asyncio.run(instance.asy_main())
        instance.main()
