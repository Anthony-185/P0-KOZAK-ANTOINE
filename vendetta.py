the_wolf = r"""
Art by Blazej Kozlowski       __
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
# Vendetta module, create a tkinter interface, wrap the functions
#     count the calls, and more
import tkinter
import time
import asyncio
import random

print(the_wolf)

class Vendetta:

    deja = False
    
    def __init__(self):
        
        if Vendetta.deja:
            print('already initied')
            return
        
        Vendetta.saved_print = print # <----------------------- saving print()
        
        self.tk = tkinter.Tk()
        self.frame = tkinter.Frame(
            self.tk,
            bg = 'cyan')
        self.frame.grid(row = 0, column = 0, sticky = 'n')
        self.canvas = tkinter.Canvas(
            self.frame,
            width = 400,
            height = 300,
            bg = 'black')
        self.canvas.grid(row = 0, column = 0)
        self.label = tkinter.Label(
            self.frame,
            bg = 'black',
            anchor = 'nw',
            font = ("Terminal", -12),
            justify = 'left',
            fg = 'cyan',
            width = 80,
            wraplength = 400)
        self.label.grid(row = 1, column = 0)
        
        list_x, list_y = [x for x in range(40, 360, 10)], [290] * 32
        coord = []
        for x, y in zip(list_x, list_y): coord.extend([x ,y])
        self.time_line = self.canvas.create_line(
            coord, fill = 'cyan')
        
        self.eta = time.time()
        self.logged_function = {}
        self.check_statement = []
        Vendetta.deja = True

    @staticmethod
    def saved_print():
        ''' copy of print function'''
        ... # <--------------------------------- define if Vendetta is initied
    
    def check(self, statement, *, get = False):
        ''' home-made assert improved '''
        try:
            result = eval(statement)
        except Exception as error:
            result = error
            print('<!> V.check', error, ':', statement)
        else:
            if result is False:
                print('<.> V.check warning :', statement, 'is', result)
            elif get:
                return result
        finally:
            self.check_statement.append((statement, result))

    def write(self, msg): # bug >> print( {str(x):x for x in range(500)} )
        ''' to redirect print in Vendetta
        
        print overwrite, stdout in tkinter Label
        ---> V.label['text']'''
        to_print = self.label['text']
        if len(msg) > 80:
            i = 0
            for index, character in enumerate(msg):
                if character == '\n': i = 0 ; continue
                i += 1
                if i > 80: msg = msg[:index] + '\n' + msg[index:] ; i = 0
        if msg == '\n':
            to_print += msg
            if to_print.count('\n') >= 26:
                to_print = to_print[to_print.find('\n') + 1:]
        elif '\n' in msg:
            to_print = to_print.split('\n') + msg.split('\n')
            to_print = '\n'.join(to_print[-26:])
        else:
            to_print += msg
        assert to_print.count('\n') < 26, AssertionError('Vendetta write')
        self.label['text'] = to_print
        if '\n' in msg: self.tk.update() # <- update tk only if new line
        
    def work(self):
        current = time.time()
        elapse_time = int((current - self.eta) * 32)
        if elapse_time > 32:
            coord = self.canvas.coords(V.time_line)
            coord[1::2] = [290] * len(coord[1::2])
            self.canvas.coords(V.time_line, coord)
            self.eta = current
        elif elapse_time < 1:
            pass
        else:
            coord = self.canvas.coords(V.time_line).copy()
            coord_y = coord[1::2]
            coord_y = [290] * (elapse_time - 1)\
                    + [270]\
                    + coord_y[:-elapse_time]
            coord[1::2] = coord_y
            self.canvas.coords(V.time_line, coord)
            self.eta = current
        self.tk.update()

    def for_vendetta(self, func):
        ''' wrapper for log function '''
        def function_wrapped(*args, **kvargs):
            ''' log the function call
            
            log with args and kwargs
            and have a called counter'''
            log = self.logged_function
            name = func.__name__
            if name not in log:
                log[name] = {'call': 0}
            log[name]['last'] = {
                'args': (args),
                'kvargs': (kvargs),
                'result': func(*args, **kvargs)}
            log[name]['call'] += 1
            return log[name]['last']['result']
        return function_wrapped

V = Vendetta()

def print(*args, **kvargs):
    kvargs.update({'file': V})
    Vendetta.saved_print(*args, **kvargs)

print(the_wolf)
if __name__ == '__main__':
    time.sleep(0.7)
    print(3*'\n')
    for i in range(0, 7 + 1) : print( i * '_', i)
    V.check('1==1')
    V.check('1==0')
    V.check('1//0')    print( ('*' + '_' * 9) * 16)
    print([i for i in range(1, 117 + 1)])
    print('< End of Vendetta >'.center(80, '-'))
# _____________________________________________________________________________
#   image generated by http://www.glassgiant.com/ascii/ (and custom by me)
# _____________________________________________________________________________
#                            . .               =                               
#                              $               . .  .                          
#                           .  .N            .N. .                             
#                       .  .. M O.           .7 8     ,                        
#                        N.M. N ..           . .D. D.D.                        
#                      N M.N.:NI             ..NN..N,N I                       
#                  .   D.,NMMNMMN            .MNNMMNN~ D   ,                   
#                   D  .NMMNMNMNM             N,MMNNDNM   M                    
#                    N   N~MMNN..             . MNNM,D.  N                     
#                     D .DNNMNMN.             .MMNNNND..N                      
#                    .MM8NNNMNNM.             .MDNNNNN$MN                      
#                    .=NNMNMMMMM              .MMNNNMMNM~                      
#                     NMMMNMMMNMN:           +MMMMNNNMNNN                      
#                     DMMNNNNNNNMM.         .MMMMMMMMMMND                      
#                      MMMNMMMMMMMM         NMMMMMNMNMMN                       
#                     NNMMMMMMNNNMN         MMMMMMMNNMNNN                      
#                    DMMMMNNMMMMMNN         MNNMMMMMMMNNNO                     
#                    :NNDMMMMMMNDM.         .DNMMMMMMMDMN=                     
#                    .MMNNMMNMMN.              NMMNNMNMMM                      
#                    .MNMMM.MMM.   .MMM..       MMM.MNNMD                      
#                     MNMN:NMM.  NMMDNNNMM.     .MMM=MNNM                      
#                   DD.NMMMMMN     .MNMMMNMN     MMMMMDM NN                    
#                  .ND DNMNMNM     ,MMMMMMON    .NNMMMMN MD                    
#                      .MNNNMNMMD   NMMMMMM.  8MMMMMMNN.                       
#                      . NDNDNNN.D. . ..     O NMMNMMM                         
#                        .8DNDDN.M,         .M NMMNMM.                         
#                      .17  17  .17.  7  .11117  .111117                          
#                      .17  17  .117. 7  .117    .17                              
#                      .17  17  .7 17.7    .117  .17                              
#                      .111117  .7  117  .11117  .111117                          
#                   .       7.NDD.           .DDN.D      .                     
#                    7       =MNN+ .        .:N:DZ       ?                     
#                    .,..    ~DZ.DO  .   .  DD..N.     ?~                      
#                    . 8  ...?.  D DD .. .NDDN.: O. .. ~..                     
#                          N   ND?N.D8N~8DDDDNDO ..D ..,                       
#                        .,I $. DN.DD7D.DDDNNDD. 7.+:                          
#                         D..8 .8DD.DDDD.8ND8.N  8 .8.                         
#                         ..,..Z .D,,ZD8DZ:.8.  D+=                            
#                             :+..=.?...$?:8.7.,~                              
#                               .DDD? .,..?D8D                                 
#                                 $88DDDDD88                                   
#                                    OD8D8
# _____________________________________________________________________________