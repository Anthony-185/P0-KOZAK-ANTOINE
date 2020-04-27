the_wolf = r"""Art by Blazej Kozlowski       __
                            .d$$b
program by                .' TO$;\
   Anthony Cosaque       /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-'       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   '      .d$$$P' |\^'l
             .'           `T$P^'''''  :
         ._.'      _.'                ;
      `-.-'.-'-' ._.       _.-'    .-'
    `.-' _____  ._              .-'
   -(.g$$$$$$$b.              .'
     ''^^T$$$P^)            .(:
       _/  -'  /.'         /:/;
    ._.'-'`-'  ')/         /;/;
 `-.-'..--''   ' /         /  ;
.-' ..--''        -'          :
..--''--.-'         (\      .-(\
  ..--''              `-\(\/;`
    _.                      :
                            ;`-
                           :\ """
from vendetta import *
# print(the_wolf)
import asyncio



class calculette:
    ...

class MainWindow:

    def __init__(self):
    
        self.frame = tkinter.Frame(
            V.tk,
            background = 'orange',
            width = 440,
            height = 640)
        self.frame.grid(row = 0, column = V.tk.grid_size()[0] + 1)
        # self.frame.grid_propagate(0)
        
        canvas = tkinter.Canvas(
            self.frame,
            background = 'black',
            width = 400,
            height = 100)
        canvas.grid(row = 0, column = 1, columnspan = 4)
        self.frame.update() ; time.sleep(0.01)
        
        dict_button = {}
            
        config = {'background': 'white', 'foreground': 'black'}
        
        for pos, symbol in zip(range(1, 4 + 1), '?/*-'): #  [ ? ] [ / ] [ * ] [ - ]
            button = tkinter.Button(
                self.frame,
                width = 10,
                height = 5,
                text = symbol, **config)
            button.grid(row = 1, column = pos)
            dict_button[symbol] = button
            self.frame.update() ; time.sleep(0.01)
            
        for pos in range(9): # <--------------------------- [ 7 ] [ 8 ] [ 9 ] 
            button = tkinter.Button(  # [ 00000000 ]      # [ 4 ] [ 5 ] [ 6 ]
                self.frame,           # [?][/][*][-]      # [ 1 ] [ 2 ] [ 3 ]
                **config,             # [7][8][9][+] < 
                width = 10,           # [4][5][6][+] <
                height = 5,           # [1][2][3][=] <
                text = str(pos + 1))  # [  0 ][.][=]
            button.grid(              #           ^
                row = 3 - (pos // 3) + 2, # negate 3, add 2
                column = pos % 3 + 1) # add 1 for first column
            symbol = str(pos + 1)
            dict_button[symbol] = button
            self.frame.update() ; time.sleep(0.01)
            
        button = tkinter.Button(  # [ 00000000 ]
            self.frame,           # [?][/][*][-]
            **config,             # [7][8][9][+] <
            width = 10,           # [4][5][6][+] <
            height = 11,          # [1][2][3][=]
            text = '+')           # [  0 ][.][=]
        symbol = '+'              #           ^
        button.grid(row = 3, column = 4, rowspan = 2)
        dict_button[symbol] = button
        self.frame.update() ; time.sleep(0.01)
        
        button = tkinter.Button(  # [ 00000000 ]
            self.frame,           # [?][/][*][-]
            **config,             # [7][8][9][+] 
            width = 10,           # [4][5][6][+] 
            height = 11,          # [1][2][3][=] <
            text = '=')           # [  0 ][.][=] <
        symbol = '='              #           ^
        button.grid(row = 5, column = 4, rowspan = 2)
        dict_button[symbol] = button
        self.frame.update() ; time.sleep(0.01)
        
        button = tkinter.Button(
            self.frame,
            **config,
            width = 10,
            height = 5,
            text = '.')
        symbol = '.'
        button.grid(row = 6, column = 3)
        dict_button[symbol] = button
        self.frame.update() ; time.sleep(0.01)
        
        button = tkinter.Button(
            self.frame,
            **config,
            width = 24, # increasing aspect
            height = 5,
            text = '0')
        symbol = '0'
        button.grid(row = 6, column = 1, columnspan = 2)
        dict_button[symbol] = button
        self.frame.update() ; time.sleep(0.01)
        
        for each_button in dict_button.values():
            each_button['background'] = 'black'
            each_button['foreground'] = 'cyan'
            self.frame.update() ; time.sleep(0.02)
        self.frame['background'] = 'black'
        
        self.dict_button = dict_button
        
    async def asy_main(self):
        
        for button in dict_button.copy().values():
        
            each_button['background'] = '#222222'
            await asyncio.sleep(0.343)
            each_button['background'] = '#000000'
            
    


if __name__ == '__main__' :
    
    MainWindow()
    
    module_enable = {}
    for module in (
        'other_anim',
        'python_interface',
        # 'sql_connector_try',
        'anim_with_lines',
        'anim',
        ):
        try:
            exec('import ' + module)
        except ModuleNotFoundError:
            msg = f'<!> module {module} not found !'
            print(msg)
            input(str(' ' + msg + ' > ok ?').center(78, '/'))
            module_enable[module] = False
        else:
            module_enable[module] = instance = eval(module + '.MainWindow()')
            print(f'<!> module {module} enabled !')
    print('starting while loop')
    
    # async def update():
        # while 1:
            # V.tk.update()
            # await asyncio.sleep(0.04)
    
    async def main_async_loop():
    
        # task0 = asyncio.create_task(
            # update())
        task1 = asyncio.create_task(
            module_enable['python_interface'].asy_main())
        task2 = asyncio.create_task(
            module_enable['anim_with_lines'].asy_main())
        task3 = asyncio.create_task(
            module_enable['anim'].asy_main())
        task4 = asyncio.create_task(
            module_enable['other_anim'].asy_main())
        
        await asyncio.sleep(0.01)
        task1_is_finish = task1.done()
        while not task1_is_finish:
            if task2.done():
                task2 = asyncio.create_task(
                    module_enable['anim_with_lines'].asy_main())
            # V.tk.update()
            await asyncio.sleep(0)
            task1_is_finish = task1.done()
        await task2 ; assert task1.done() ; await task3 ; await task4

    if module_enable['python_interface'] and module_enable['anim_with_lines']:
        try:
            while 1:
                asyncio.run(main_async_loop())
        except Exception as e:
            print('awaiting')
            # task0.cancel()
            task1.cancel()
            task2.cancel()
            task3.cancel()
            print('done :', done, 'pending :', pending, 'e', e)
        finally:
            V.saved_print('so ?')