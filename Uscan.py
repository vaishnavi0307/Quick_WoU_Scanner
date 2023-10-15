from pytermgui import tim
from __init__ import VERSION, PATHS, MODS
from Modules import __init__ as Scan
from Modules.colors import Colors
from Modules.dork.bingdorker import bingdorker
import threading

# Copyright (C) 2023 Nano / github.com/l4tt
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details. https://www.gnu.org/licenses/


BANNER = f"""
                ╦ ╦┌─┐┌─┐┌─┐┌┐┌
                ║ ║└─┐│  ├─┤│││
                ╚═╝└─┘└─┘┴ ┴┘└┘
                        \033[1;91m スキャナー\033[00m
    """
HELP_MENU = f"""
                                    
                              
             ╔══════════════════════════════════════════════════════════{Colors.WHITE}╗
       [blink2 red]U{Colors.RESET}     ║{Colors.WHITE}                                                          ║{Colors.WHITE}
       [bold blue]S[white]     ║{Colors.WHITE}   1. vulnscan - scans vulns in a target [reset]                 ║
       [red]C[white]     ║{Colors.WHITE}   2. autoscan - autodorks                                ║{Colors.WHITE}
       [blue]A[white]     ║{Colors.WHITE}                                                          ║{Colors.WHITE}
       [red]N[white]     ╚══════════════════════════════════════════════════════════{Colors.WHITE}╝

    """



if __name__ == '__main__':
    print(BANNER)
    try:
        while True:
            USER_MENU_INPUT = input(f'[ {Colors.RED}{Colors.ITALIC}$can{Colors.WHITE}{Colors.RESET} ] {Colors.BRIGHT}>>{Colors.WHITE} ')
            if USER_MENU_INPUT == "": print('Invalid command, please type help')
            elif USER_MENU_INPUT == 'help': tim.print(HELP_MENU)
            elif USER_MENU_INPUT == '1':
                user_site_input = input(f'[ {Colors.RED}{Colors.ITALIC}Url{Colors.WHITE}{Colors.RESET} ] {Colors.BRIGHT}>>{Colors.WHITE} ')
                t1 = threading.Thread(target=Scan, args=[user_site_input])
                t1.start()
                t1.join()
            elif USER_MENU_INPUT == '2':
                for urls in bingdorker():
                    t2 = threading.Thread(target=Scan, args=[urls])
                    t2.start()
                    t2.join()
    except (KeyboardInterrupt):
        exit(f"\n\nExiting {Colors.RED2}Uscan{Colors.WHITE}...\n")