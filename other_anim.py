from vendetta import *
import random

if __name__ == '__main__' : print(the_wolf)

class MainWindow:

    HEIGHT = 620

    def __init__(self):
        
        self.frame = tkinter.Frame(
            V.tk,
            background = 'cyan',
            width = 400,
            height = 300)
        self.frame.grid(row = 0, column = V.tk.grid_size()[0] + 1)
            
        self.canvas = tkinter.Canvas(
            self.frame,
            background = 'black',
            width = 400,
            height = MainWindow.HEIGHT)
        self.canvas.grid(row = 0, column = 0)
        
        self.target_area = self.canvas.create_rectangle(
            0,0,10,10, outline = '#700', dash = (3, 7), fill = '')
        self.target_zone = self.canvas.create_rectangle(
            0,0,10,10, outline = '#117', dash = (3, 7), fill = '#077')
        self.target_goal = self.canvas.create_oval(
            0,0,10,10, fill = '#700')
        
        self.all_x = []
        self.all_y = []
        self.canvas_element = []
        
        for _ in range(17):
            self.random_squar()
            self.canvas.update() ; time.sleep(0.01)
        
        self.canvas.tag_lower('coord')
            
        for _ in range(20):
            self.canvas.itemconfig(
                random.choice(self.canvas_element),
                outline = 'cyan')

    def main(self):
        
        # print('in asy loop')
        # asyncio.run(self.asy_loop())
        # print('asy loop ended')
        
        # for i in range(20):
            # print('beginning loop %d'.center(25).center(78, '=') % i)
            # asyncio.run(self.asy_main())
            
        asyncio.run(self.asy_main())
            
    async def asy_main(self):
    
        if __name__ != '__main__':
            await asyncio.create_task(self.asy_loop())
            return
        
        task0 = asyncio.create_task(self.asy_update())
        task1 = asyncio.create_task(self.random_select())
        task2 = asyncio.create_task(self.random_outline())
        
        done, pending = await asyncio.wait(
            {task1, task2}, return_when='FIRST_COMPLETED')
        
        i = 0
        while pending and i <= 20:
            # print(pending, i)
            i += 1 ; a = 'i >= 20' ; print(a) if eval(a) else ...
            done, pending = await asyncio.wait(
                {task1, task2}, return_when='FIRST_COMPLETED')
            if not pending: print('BREAKING') ; break
            if task1 in done: task1 = asyncio.create_task(self.random_select())
            if task2 in done: task2 = asyncio.create_task(self.random_outline())
            
            self.canvas.update()
            await asyncio.sleep(0.07)
            
        print('<<< Ending with : ', done, pending, '>>>', sep='\n')
        done, pending = await asyncio.wait(
            {task1, task2}, return_when='ALL_COMPLETED')
        
        task0.cancel()
            
        return
        
            
    async def asy_loop(self):
    
        task0 = asyncio.create_task(self.asy_update())
        
        # for _ in '1234567':
            # task4 = asyncio.create_task(self.random_move(), name = 'task4')
            # await task4
    
        task1 = asyncio.create_task(self.random_select(), name = 'task1')
        task2 = asyncio.create_task(self.random_outline(), name = 'task2')
        task3 = asyncio.create_task(self.select_coord(), name = 'task3')
        task4 = asyncio.create_task(self.random_move(), name = 'task4')
        
        old_task = None
        while 1:
            done, pending = await asyncio.wait(
                {task1, task2, task3}, return_when='FIRST_COMPLETED')
            if task1.done():
                task1 = asyncio.create_task(self.random_select(),
                name = 'task1')
            if task2.done():
                task2 = asyncio.create_task(self.random_outline(),
                name = 'task2')
            if task3.done():
                task3 = asyncio.create_task(self.select_coord(),
                name = 'task3')
            if task4.done():
                task4 = asyncio.create_task(self.random_move(),
                name = 'task4')

            if len(done) == 1:
                task = done.copy().pop().get_name()
                if old_task == task:
                    print('+', end = '')
                else:
                    print('\n', task)
                old_task = task
            else:
                print()
                for i, task in enumerate(done):
                    print(i, task.get_name())
        await asyncio.sleep(0)
        
            
    async def asy_update(self):
    
        while 1:
            
            self.canvas.update()
            await asyncio.sleep(0.04)
        
    async def select_coord(self):
    
        canvas = self.canvas
        for rec in canvas.find_withtag('coord'):
            canvas.itemconfig(rec, fill = '#343')
            await asyncio.sleep(0.343)
            canvas.itemconfig(rec, fill = '')
        
    async def appear(self):
        ...
        
    async def disappear(self):
        ...
        
    async def light_the_place(self):
        ...
        
    async def random_move(self):
    
        limit_x, limit_y = self.get_coord_canvas()
        for element in self.canvas_element:
            self.canvas.itemconfig(element,
                dash = (4,6), outline = 'white', fill = '#007')
            self.canvas.tkraise(element)
            self.canvas.tkraise(self.target_area)
            ax, ay, bx, by = coord = self.canvas.coords(element)
            move = random.choice('ax ay bx by'.split())
            d = delta = 10
            if   move == 'ax':
                if ax < bx:
                    area = [0, bx]
                else:
                    area = [bx, limit_x]
                coord[0] = random.randrange(area[0] + d, area[1], d)
                area = area[0], coord[1]-5, area[1], coord[1]+5
                #    = area[0], ay - 5    , area[1], ay + 5
            elif move == 'ay':
                if ay < by:
                    area = [0, by]
                else:
                    area = [by, limit_y]
                coord[1] = random.randrange(area[0] + d, area[1], d)
                area = coord[0]-5, area[0], coord[0]+5, area[1]
            elif move == 'bx':
                if bx < ax:
                    area = [0, ax]
                else:
                    area = [ax, limit_x]
                coord[2] = random.randrange(area[0] + d, area[1], d)
                area = area[0], coord[3]-5, area[1], coord[3]+5
            elif move == 'by':
                if by < ay:
                    area = [0, ay]
                else:
                    area = [ay, limit_y]
                coord[3] = random.randrange(area[0] + d, area[1], d)
                area = coord[2]-5, area[0], coord[2]+5, area[1] 
            else:
                for _ in 'xxxxx':
                    print('wtf ?'.center(78, '*'))
                    await asyncio.sleep(0.343)
            
            # print('move :', move, 'area :', area)
            self.canvas.coords(self.target_area, area)
            await asyncio.sleep(3.43)
            
            msg = ' '.join([f'{int(i): >4}' for i in (ax, ay, bx, by)])
            # print('init :', msg)
            msg = ' '.join([f'{int(i): >4}' for i in coord])
            # print('move :', msg)
            self.canvas.coords(element, coord)
            await asyncio.sleep(1.17)
            
            self.canvas.itemconfig(element, dash = (), fill = '')
            self.canvas.coords(self.target_area, 0,0,10,10)
            await asyncio.sleep(1.17)
            
    async def random_move(self):
            
        limit_x, limit_y = self.get_coord_canvas()
        for element in self.canvas_element:
        
            # print('=' * 78)
            self.canvas.itemconfig(element,
                dash = (4,6), outline = 'white', fill = '#007')
            self.canvas.tkraise(element)
            self.canvas.tkraise(self.target_area)
            self.canvas.tkraise(self.target_goal)
            
            coord = self.canvas.coords(element)
            pAB = random.randrange(2)
            pXY = random.randrange(2)
            i = pAB * 2 + pXY
            a = coord[    pAB  * 2 + pXY]
            b = coord[int(not(pAB)) * 2 + pXY]
            # print('pAB : %d, pXY : %d, i : %d' % (pAB, pXY, i))
            # print(f'a = pAB * 2 + pXY : {pAB * 2} + {pXY} = {pAB  * 2 + pXY}')
            # print(f'b = not(pAB) * 2 + pXY : {int(not(pAB)) * 2} + {pXY} = {int(not(pAB))  * 2 + pXY}')
            
            ax, ay, bx, by = coord # -------------------------------- copied !!
            move = 'ax ay bx by'.split()[i]
            d = delta = 10
            if   move == 'ax':
                area = [0, bx] if ax < bx else [bx, limit_x]
                # coord[0] = random.randrange(area[0] + d, area[1], d)
                area = area[0], coord[1]-5, area[1], coord[3]+5
            elif move == 'ay':
                area = [0, by] if ay < by else [by, limit_y]
                # coord[1] = random.randrange(area[0] + d, area[1], d)
                area = coord[0]-5, area[0], coord[2]+5, area[1]
            elif move == 'bx':
                area = [0, ax] if bx < ax else [ax, limit_x]
                # coord[2] = random.randrange(area[0] + d, area[1], d)
                area = area[0], coord[1]-5, area[1], coord[3]+5
            elif move == 'by':
                area = [0, ay] if by < ay else [ay, limit_y]
                # coord[3] = random.randrange(area[0] + d, area[1], d)
                area = coord[0]-5, area[0], coord[2]+5, area[1] 
            self.canvas.coords(self.target_zone, area)
            await asyncio.sleep(0.343)
            
            if pAB:
                o = coord[2]-5, coord[3]-5, coord[2]+5, coord[3]+5
            else:
                o = coord[0]-5, coord[1]-5, coord[0]+5, coord[1]+5
            self.canvas.coords(self.target_goal, o)
            # print('pAB :', pAB,'pXY :', pXY, 'i a b :', i, a, b)
            # print('coord :', coord)
            # print('o :', o)
            await asyncio.sleep(0.343)
            
            
            
            if a < b:
                area = [0, b]
            else:
                area = [b, limit_y if pXY else limit_x]
            area[0] += 10
            # print(area)
            
            if pXY:
                zone =  coord[pAB * 2 + (not(pXY))] - 5, area[1], \
                        coord[pAB * 2 + (not(pXY))] + 5, area[0]
            else:
                zone =  area[1], coord[pAB * 2 + (not(pXY))] - 5, \
                        area[0], coord[pAB * 2 + (not(pXY))] + 5
            self.canvas.coords(self.target_area, zone)
            # print(zone)
            await asyncio.sleep(0.343)
            
            n = coord[pAB * 2 + pXY] = random.randrange(*area, 10)
            if pXY:
                o = coord[pAB * 2 + (not(pXY))], n
            else:
                o = n, coord[pAB * 2 + (not(pXY))]
            o = o[0] - 5, o[1] - 5, o[0] + 5, o[1] + 5
            self.canvas.coords(self.target_goal, o)
            # print(o)
            await asyncio.sleep(0.343)
            
            self.canvas.coords(element, coord)
            await asyncio.sleep(0.343)
            
            self.canvas.coords(self.target_goal, 0,0,10,10)
            self.canvas.coords(self.target_area, 0,0,10,10)
            self.canvas.itemconfig(element, dash = (), fill = '')
        
    async def random_select(self, sleep = 3.43):
        '''fill in blue one canvas element at a time'''
    
        for element in self.canvas_element:
            self.canvas.itemconfig(element, fill = '#117')
            await asyncio.sleep(sleep)
            self.canvas.itemconfig(element, fill = '')
        
    async def random_outline(self, sleep = 0.343):
        '''change outline's color of all canvas element
        one canvas element at a time'''
        
        for element in self.canvas_element:
            self.canvas.itemconfig(element,
                outline = self.random_cyan())
            await asyncio.sleep(sleep)
    
    def random_color(self):
    
        color = ['#']
        for _ in 'rgb':
            rgb = hex(random.randrange(256))[2:] # remove '0x' !
            rgb = f'{rgb:0>2}' # '2' >>> '02'
            color += [rgb]
        return ''.join(color)
        
    def random_cyan(self):
    
        color = ['#', '00']
        for _ in 'green', 'blue':
            rgb = hex(random.randrange(256))[2:] # remove '0x' !
            rgb = f'{rgb:0>2}' # '2' >>> '02'
            color += [rgb]
        return ''.join(color)
        
    def get_coord_canvas(self):
        '''return x, y as integrer'''
        
        limit_x = self.canvas.config('width')[4]
        limit_y = self.canvas.config('height')[4]
        delta = 10
        if not (limit_x.isdigit() and limit_y.isdigit()):
            limit_x = 400
            limit_y = 620
            for _ in '123': print('fuck !'.center(78, '/')) ; time.sleep(1)
        else:
            limit_x = int(limit_x)
            limit_y = int(limit_y)
        return limit_x, limit_y


    def random_squar3(self): # V1
            
        limit_x, limit_y = self.get_coord_canvas()
        
        limit_x = {*range(delta, limit_x, delta)}
        limit_y = {*range(delta, limit_y, delta)}
        
        x1, x2 = random.sample(limit_x, 2)
        y1, y2 = random.sample(limit_y, 2)

        rectangle = self.canvas.create_rectangle(
            x1, y1, x2, y2,
            outline = self.random_cyan(), activefill = 'green')
        self.canvas_element.append(rectangle)
        
    def random_squar2(self): # V1
    
        x1 = random.choice(range(100, 300, 10))
        x2 = random.choice(range( x1, 310, 10)) # 310 !
        y1 = random.choice(range(100, 300, 10))
        y2 = random.choice(range( y1, 310, 10)) # 310 !
        color = self.random_color()

        rectangle = self.canvas.create_rectangle(
            x1, x2, y1, y2, outline = color, activefill = 'lightgreen')
        self.canvas_element.append(rectangle)
        
    def random_squar1(self, mode = None): # V2
    
        x1, x2, y1, y2 = [random.choice(range(100, 310, 10)) for _ in '0123']
        color = self.random_color()

        if mode == None:
            rectangle = self.canvas.create_rectangle(
                x1, x2, y1, y2, outline = color)
        else:
            rectangle = self.canvas.create_rectangle(
                x1, x2, y1, y2, fill = color)
        self.canvas_element.append(rectangle)
        
    def random_squar(self, nb = 1): # V4

        condition = (len(self.all_x) >= nb * 2) and (len(self.all_y) >= nb * 2)
        if not condition:
            limit_x, limit_y = self.get_coord_canvas()
            delta = 10
            self.all_x = {*range(delta, limit_x, delta)}
            self.all_y = {*range(delta, limit_y, delta)}
        
        for _ in nb * 'x':
        
            x1, x2 = random.sample(self.all_x, 2)
            y1, y2 = random.sample(self.all_y, 2)
            self.all_x -= {x1, x2}
            self.all_y -= {y1, y2}
            
            coord1 = self.canvas.create_rectangle(
                0, 0, x1, y1,
                outline = '#343', tag = 'coord',
                fill = '', activefill = '#343', dash = (4,6))
            coord2 = self.canvas.create_rectangle(
                0, 0, x2, y2,
                outline = '#343', tag = 'coord',
                fill = '', activefill = '#343', dash = (4,6))

            rectangle = self.canvas.create_rectangle(
                x1, y1, x2, y2,
                outline = self.random_cyan())
            self.canvas_element.append(rectangle)
    
if __name__ == '__main__':

    instance = MainWindow()
    instance.main()