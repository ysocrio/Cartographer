import sys, tty, termios

class WASD_control:
    """
    controls a chassis using input from the python terminal
    """

    def __init__(self):
        #intial stuffs
        pass

    def update(self):
        key = 0
        key = self.getch()
        if key == "w":
            return self.forward()
        elif key == "s":
            return self.back()
        elif key == "a":
            return self.left()
        elif key == "d":
            return self.right()
        else:
            return [0,0]

    def forward(self):
        return [50, -50]

    def back(self):
        return [-50, 50]

    def left(self):
        return [-50,-50]

    def right(self):
        return [50, 50]

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
