from vendetta import *

if __name__ == '__main__' :


    list_module = [
        # 'calculette_exemple', ## not woking very well actually
        'other_anim',
        'python_interface',
        'sql_connector_try', ## not woking very well actually
        'anim_with_lines',
        'anim']
        
    # random.shuffle(list_module)
    # list_module = list_module[:3]
        
    module_enable = {}
    
    for module in list_module:
        try:
            exec('import ' + module)
        except ModuleNotFoundError:
            msg = f'<!> {module} not found !'
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
        while 1:
            done, pending = await asyncio.wait(
                {task1, task2, task3, task4}, return_when='FIRST_COMPLETED')
            if task1.done():
                task1 = asyncio.create_task(
                    module_enable['python_interface'].asy_main())
            if task2.done():
                task2 = asyncio.create_task(
                    module_enable['anim_with_lines'].asy_main())
            if task3.done():
                task3 = asyncio.create_task(
                    module_enable['anim'].asy_main())
            if task4.done():
                task4 = asyncio.create_task(
                    module_enable['other_anim'].asy_main())
            await asyncio.sleep(0)
            try:
                for task in done:
                    print(task.get_name())
            except:
                task1.cancel()
                task2.cancel()
                task3.cancel()
                task4.cancel()
                break
                
        print( task1.done(), task2.done(), task3.done(), task4.done() )

    if module_enable['python_interface'] and module_enable['anim_with_lines']:
        try:
            asyncio.run(main_async_loop())
        except Exception as e:
            V.saved_print(f'*** break because of : {e} ***'.center(78))
        finally:
            V.saved_print(' END OF FILE '.center(78, '/'))