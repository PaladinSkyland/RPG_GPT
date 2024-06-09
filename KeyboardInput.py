import sys
import os

if os.name == 'posix':
    import tty
    import termios
elif os.name == 'nt':
    import msvcrt

class KeyboardInput:
    def __init__(self):
        if os.name == 'posix':
            self.key_mapping = {
                126: 'delete',
                127: 'backspace',
                10: 'return',
                32: 'space',
                27: 'escape',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left'
            }
        elif os.name == 'nt':
            self.key_mapping = {
                83: 'delete',
                8: 'backspace',
                13: 'return',
                32: 'space',
                27: 'escape',
                72: 'up',
                80: 'down',
                77: 'right',
                75: 'left'
            }

    def __enter__(self):
        if os.name == 'posix':
            self.old_settings = termios.tcgetattr(sys.stdin)
            tty.setcbreak(sys.stdin.fileno())
        return self

    def __exit__(self, type, value, traceback):
        if os.name == 'posix':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def getkey(self):
        if os.name == 'posix':
            b = os.read(sys.stdin.fileno(), 5).decode()
            if b.isprintable():
                return b
            elif len(b) > 1:
                b = b[-1]
        elif os.name == 'nt':
            b = msvcrt.getch().decode()
            if b.isprintable():
                return b
            elif b == '\xe0' or b == '\x00':
                b = msvcrt.getch().decode()
        else:
            raise NotImplementedError("This OS is not supported.")
        return self.key_mapping.get(ord(b), b)