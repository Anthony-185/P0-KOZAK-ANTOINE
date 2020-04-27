from vendetta import *

if __name__ == '__main__' : print(the_wolf)

import time
import asyncio
import random


class HUD:

    def __init__(self, x = 400, y = 280):
        
        self.tk_element = []
        
        line = V.canvas.create_line
        pos =  10,  20,  20,  10, 100,  10
        config = {'fill': 'cyan'}
        self.tk_element += [
            line( 10,  20,  20,  10, 100,  10, **config),
            line(390,  20, 380,  10, 300,  10, **config),
            line( 10, 260,  20, 270, 100, 270, **config),
            line(390, 260, 380, 270, 300, 270, **config)
            ]


class AimPoint:

    def __init__(self, x, y):
    
        self.obj = []
        
        line = V.canvas.create_line
        config = {'fill': 'cyan'}
        self.obj += [
            line(x, y - 50, x, y - 10, **config),
            line(x + 10, y, x, y + 10, x, y + 50, **config),
            line(x - 50, y, x - 10, y, **config),
            ]

        oval = V.canvas.create_oval
        config.update({'outline': 'green'}) 
        self.obj += [
            oval(x +  5, y - 50 +  5, x + 10, y - 50 + 10, **config),
            oval(x +  5, y - 50 + 15, x + 10, y - 50 + 20, **config)
            ]
        
        self.target = V.canvas.create_arc(
            10, 10, 20, 20, fill = '', outline = 'orange', extent = -45)
        
        V.canvas.update()
    
    def move(self, x = 0, y = 0):
    
        if x != 0 or y != 0:
            for obj in self.obj:
                coord = V.canvas.coords(obj)
                for i, j in enumerate(coord):
                    coord[i] += x if i % 2 == 0 else y
                V.canvas.coords(obj, coord)
            V.canvas.update()
            
    def give_coord(self):
        x = int(V.canvas.coords(self.obj[0])[0])
        y = int(V.canvas.coords(self.obj[1])[1])
        return x, y
            
    async def asy_move(self, x = 0, y = 0, slow = 0):
        
        if x != 0:
            incre = 1 if x > 0 else -1
            for _ in range(0, x, incre):
                for obj in self.obj:
                    coord = V.canvas.coords(obj)
                    for i, j in enumerate(coord):
                        coord[i] += incre if i % 2 == 0 else 0
                    V.canvas.coords(obj, coord)
                await asyncio.sleep(slow)
                
        if y != 0:
            incre = 1 if y > 0 else -1
            for _ in range(0, y, incre):
                for obj in self.obj:
                    coord = V.canvas.coords(obj)
                    for i, j in enumerate(coord):
                        coord[i] += 0 if i % 2 == 0 else incre
                    V.canvas.coords(obj, coord)
                await asyncio.sleep(slow)
            
    def on_off(self, mv_x = None, mv_y = None):
    
        if (mv_x != None) or (mv_y != None):
            old = V.canvas.itemconfig(self.target)['outline'][4]
            if old == 'orange':
                V.canvas.itemconfig(self.target, outline = 'green')
                V.canvas.coords(self.target,
                    mv_x - 10, mv_y - 10, mv_x + 10, mv_y + 10)
            else:
                V.canvas.itemconfig(self.target, outline = 'orange')
                V.canvas.coords(self.target,
                    10, 10, 20, 20)
    
        for obj in self.obj:
            old = V.canvas.itemconfig(obj)['fill'][4]
            new = 'cyan' if old != 'cyan' else 'orange'
            V.canvas.itemconfig(obj, fill = new)
        V.canvas.update()

class MainWindow:

    def __init__(self):
    
        l = self.l = []
        for x in range(20, 380, 10):
            if not (x - 20) % 50:
                l += [V.canvas.create_oval(x, 20, x + 10, 30, outline='cyan')]
            else:
                l += [V.canvas.create_rectangle(x, 23, x + 10, 27, outline='cyan')]
        
        self.aim = AimPoint(70, 70)
        V.canvas.update()

    async def turn_point(self, keep = True):
    
        l = self.l
        if keep:
            for i in l:
                V.canvas.itemconfig(i, fill = 'green')
            V.canvas.update()
        for i in l:
            V.canvas.itemconfig(i, fill = 'cyan')
            V.canvas.update()
            await asyncio.sleep(0.03)


    async def normal_code(self):
    
        aim = AimPoint(70, 70)
        aim.on_off()
        aim.move(x = 10)
        aim.move(y = 20)
        for i in range(10):
            aim.move(x = 10)
        aim.on_off()
    
    
    def main(self):
    
        asyncio.run(self.asy_main())
    
    
    async def asy_main(self):
        
        aim = self.aim
        task1 = asyncio.create_task(self.turn_point(False))
        await asyncio.sleep(0) ; aim.on_off()
        await asyncio.sleep(0) ; aim.move(x = 10)
        await asyncio.sleep(0) ; aim.move(y = 20)
        for i in range(10):
            aim.move(x = 10) ; await asyncio.sleep(0)
        await asyncio.sleep(0) ; aim.on_off()
        task2 = asyncio.create_task(self.hide_obj())
        await asyncio.sleep(0) ; HUD()
        await task1
        task3 = asyncio.create_task(self.turn_point())
        done, pending = await asyncio.wait(
            {task2, task3},
            return_when=asyncio.ALL_COMPLETED)
        assert not pending
        # print(task1.done(), task2.done(), task3.done(), done, pending)
        
    
    async def hide_obj(self):

        aim = self.aim
        for _ in range(3):
            Lx = 400 # = V.canvas.winfo_geometry() arggggggggggggggggggg !!!!!!!
            Ly = 300 # = V.canvas.winfo_geometry()
            cx, cy = current_pos = aim.give_coord()
            
            rangeX = [0, Lx / 2] if cx > (Lx / 2) else [Lx / 2, Lx]
            rangeY = [0, Ly / 2] if cy > (Ly / 2) else [Ly / 2, Ly]
            
            rangeX, rangeY = [0 + 20, Lx - 20], [0 + 40, Ly - 40]
            
            r = random.randrange
            arrival_pos = ax, ay = r(*rangeX, 10), r(*rangeY, 10)
            
            x, y = ax - cx, ay - cy
            task = asyncio.create_task(self.look(x, y, ax, ay))
            await task

    async def look(self, mv_x = 60, mv_y = 80, ar_x = None, ar_y = None):
    
        aim = self.aim
        aim.on_off(ar_x, ar_y)
        task1 = asyncio.create_task(aim.asy_move(mv_x, mv_y, slow = 0.01))
        
        await asyncio.sleep(0)
        task1_is_finish = task1.done()
        
        while not task1_is_finish:
            V.canvas.update()
            await asyncio.sleep(0.01)
            task1_is_finish = task1.done()
            
        aim.on_off(ar_x, ar_y) ; await asyncio.sleep(1.17)



if __name__ == '__main__' :

    instance = MainWindow()
    instance.main()
