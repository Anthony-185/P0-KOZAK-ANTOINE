from vendetta import *
import random

if __name__ == '__main__' : print(the_wolf)

class MainWindow:

    def __init__(self):
        
        self.frame = tkinter.Frame(
            V.tk,
            background = 'cyan',
            width = 400,
            height = 300)
        self.frame.grid(row = 0, column = V.tk.grid_size()[0] + 1)
        
        self.changement = {}
        self.canvas_function()
        self.canvas_multi_obj()

    def main(self, update=True):
        for i in range(0, random.randrange(1, 7000)): # there is always an i
            self.play_with_canvas_2()
            if update: V.tk.update()
        else: print(i) # had an error, no i !!! --> RESOLVED
        self.annul_change()
        
    async def asy_main(self):
        for i in range(0, random.randrange(1, 7000)): # there is always an i
            self.play_with_canvas_2()
            self.canvas_2.update()
            await asyncio.sleep(0)
        else: print(i) # had an error, no i !!! --> RESOLVED
        self.annul_change()
        
    def canvas_function(self):
        
        r = random
        list_function = [
        lambda x : x ** r.randrange(2),
        lambda x : x ** r.randrange(3),
        lambda x : 2 * x + r.randrange(100),
        lambda x : (x + 1) * (x - 1),
        lambda x : x,
        lambda x : x * (x * r.randrange(10)),
        lambda x : x * (x + 1) * (x + 2),
        lambda x : -x + r.randrange(1000),
        lambda x : x + 1 - x / 2,
        lambda x : x // 2,
        lambda x : x % 2,
        lambda x : x // 3,
        lambda x : x % 3,
        lambda x : x ** 2 - 1,
        lambda x : x ** 2 + 2 * x - 1,
        lambda x : x ** (1 / 2) * x,
        lambda x : x ** 4 / r.randrange(1, 1000),
        lambda x : r.randrange(100) * x / r.randrange(1, 10),
        lambda x : x + 25 * x - x * x,
        lambda x : 2 * x + 10 * x // 2,
        lambda x : x if x % 2 == 0 else - x + r.randrange(300)
        ]
        
        self.canvas = tkinter.Canvas(
            self.frame,
            background = 'black')
        self.canvas.grid()
        
        list_to_show = [
            [int(f(i)) for i in range(100) if f(i) < 300]
            for f in list_function ]
        
        for i, list_result in enumerate(list_to_show):
            i += 1
            for j, value in enumerate(list_result):
                if value > 300: continue
                self.canvas.create_oval(
                    value, i * 10, value + 5, i * 10 + 5, fill= 'cyan')
            self.canvas.create_text(
                375, i * 10, anchor = 'e',
                fill = 'orange', text = len(list_result))
        V.tk.update()
        
    def canvas_multi_obj(self):
    
        self.canvas_2 = tkinter.Canvas(
            self.frame, background = 'black', height = 350)
        self.canvas_2.grid()
        
        for i in range(1 , 11):
            for j in range(1, 11):
                self.canvas_2.create_rectangle(
                    i * 10, j * 10, i * 10 + 10, j * 10 + 10, fill = 'cyan')
                self.canvas_2.create_rectangle(
                    i * 10 + 110, j * 10, i * 10 + 120, j * 10 + 10,
                    fill = '', outline = 'cyan', dash = (2,1,2))
                self.canvas_2.create_rectangle(
                    i * 10 + 220, j * 10, i * 10 + 230, j * 10 + 10,
                    fill = 'cyan', outline = 'orange', dash = (2,1))
                self.canvas_2.create_rectangle(
                    i * 10 + 1, j * 10 + 111, i * 10 + 9, j * 10 + 119,
                    fill = 'cyan')
                self.canvas_2.create_rectangle(
                    i * 10 + 111, j * 10 + 111, i * 10 + 119, j * 10 + 119,
                    fill = '', outline = 'cyan', dash = (8,1))
                self.canvas_2.create_rectangle(
                    i * 10 + 221, j * 10 + 111, i * 10 + 229, j * 10 + 119,
                    fill = '', outline='orange', dash = (8,1), width = 2)
                self.canvas_2.create_oval(
                    i * 10, j * 10 + 220, i * 10 + 10, j * 10 + 230,
                    fill = 'green')
                self.canvas_2.create_oval(
                    i * 10 + 110, j * 10 + 220, i * 10 + 120, j * 10 + 230,
                    fill = 'green', outline='cyan', activefill = 'red')
                self.canvas_2.create_polygon(
                    i * 10 + 3 + 220, j * 10 + 2 + 220,
                    i * 10 + 7 + 220, j * 10 + 2 + 220,
                    i * 10 + 9 + 220, j * 10 + 5 + 220,
                    i * 10 + 7 + 220, j * 10 + 8 + 220,
                    i * 10 + 3 + 220, j * 10 + 8 + 220,
                    i * 10 + 1 + 220, j * 10 + 5 + 220,
                    fill = 'cyan', outline = 'green')
                # V.tk.update() # <--------------------------------- enjoy !!!
    
    def play_with_canvas_2(self):
        
        item = random.choice(self.canvas_2.find_all())
        if item not in self.changement:
            self.changement[item] = self.canvas_2.itemconfig(item)
            
        color = 'purple', 'red', 'blue', 'orange', 'yellow', 'green', \
            'lightgreen', 'darkgreen', 'lightblue', 'darkblue', 'grey', \
            '', 'black', 'white', 'cyan'
        # color = 'cyan green blue lightgreen white black '.split() + ['']
            
        config = random.sample((
            # {'fill': random.choice(color)},
            {'outline': random.choice(color)},
            {'dash': random.sample(range(2, 10), random.randrange(1, 5))},
            {'width': random.randrange(3)}
        ), 1)[0]
            
        self.canvas_2.itemconfig(item, **config)
        
    def annul_change(self):
        
        for caneva_item in self.changement.keys():
            for key, list_value in self.changement[caneva_item].items():
                self.changement[caneva_item][key] = \
                    self.changement[caneva_item][key][4]
        for item, config in self.changement.items():
            self.canvas_2.itemconfig(item, **config)
            V.tk.update()
        self.changement = {}
        
if __name__ == '__main__' :
    instance = MainWindow()
    while 1:
        asyncio.run(instance.asy_main()) ; print('asyncio done')
        instance.main(update=True) ; print('normal done') # by default True