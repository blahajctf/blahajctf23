#!/usr/local/bin/python
import sys, os

# assert os.path.exists("./flag.txt")

class UnSafeCodeException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Filter Strings to make sure the following exploit cannot happen
# https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes
def safe_filter(msg):

    # Should be fine to leave out eval, after all I am already doing it
    unsafe = ['os', 'cat', 'flag', 'ls', 'system', 'popen', 'open', 'import', 'call', 'read', 'exec']

    for string in unsafe:
        if string not in msg: continue
        raise UnSafeCodeException(f"Detected unsafe conda code \'{string}\'")



print(f"""
=============================================================================
   ██████╗ ██████╗ ███╗   ██╗██████╗  █████╗     ███████╗██╗  ██╗███████╗
   ██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗    ██╔════╝╚██╗██╔╝██╔════╝
   ██║     ██║   ██║██╔██╗ ██║██║  ██║███████║    █████╗   ╚███╔╝ █████╗  
   ██║     ██║   ██║██║╚██╗██║██║  ██║██╔══██║    ██╔══╝   ██╔██╗ ██╔══╝  
   ╚██████╗╚██████╔╝██║ ╚████║██████╔╝██║  ██║    ███████╗██╔╝ ██╗███████╗
   ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚══════╝
=============================================================================
Welcome to CONDA EXE, a python shell emulator!
Brining you safe Python Shells for Remote usage.

Python {sys.version}
Type "help", "copyright", "credits" or "license" for more information.""")

while True:
    try:
        user_input = input(">>> ")
        safe_filter(user_input)
        print(eval(user_input))
    except Exception as e:
        print(e.__class__.__name__, ": ", e, sep="")
