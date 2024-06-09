import sys
import tty
import termios
import os

class KeybordInput:
    def __init__(self):
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

    def __enter__(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        return self

    def __exit__(self, type, value, traceback):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def getkey(self):
        b = os.read(sys.stdin.fileno(), 5).decode()
        if b.isprintable():
            return b
        elif len(b) > 1:
            k = ord(b[-1])
        else:
            k = ord(b)
        return self.key_mapping.get(k, chr(k))