import sys, tty, termios

class WASD_control:
    """
    controls a chassis using input from the python terminal
    """

    def __init__(self):
        #intial stuffs
        pass

    def update(self):
        key = self.getch()
        if key == "w":
            self.w()
        elif key == "s":
            self.s()
        elif key == "a":
            self.a()
        elif key == "d":
            self.d()

    def w(self):
        print("w")

    def s(self):
        print("s")

    def a(self):
        print("a")

    def d(self):
        print("d")

    def getch(self):
        # found here: https://www.raspberrypi.org/forums/viewtopic.php?p=513526
        old_settings = termios.tcgetattr(0)
        new_settings = old_settings[:]
        new_settings[3] &= ~termios.ICANON
        try:
            termios.tcsetattr(0, termios.TCSANOW, new_settings)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(0, termios.TCSANOW, old_settings)
        return ch
