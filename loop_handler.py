from global_utils import *
from menu_methods_handler import *

def input_handler(u_input:str, max_range:int):
    u_input = u_input.strip()
    try:
        u_input = int(u_input)
        if 0 <= u_input <= max_range:
            return u_input
        else:
            print(warning_out_of_range(1, max_range))
    except ValueError:
        print(default_warning())

# loop methods       
def default_menu_loop(menu_text:str, handlers:dict, func = None):
    clear_terminal()
    while True:
        max_range = len(handlers) - 1
        if func:
            func()
        print(menu_text)

        u_input = input_handler(input(input_message(max_range)), max_range)

        if u_input in handlers:
            action = handlers[u_input]
            if action is None:
                clear_terminal()
                return
            action()  
