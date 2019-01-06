import sys, tty, termios, time

class WASD_control:
    """
    controls a chassis using input from the python terminal
    """
    #max time between key presses before it turns motor off


    def __init__(self):
        #intial stuffs
        self._key_timeout = .2
        self._previous_time = 0
        self._current_time = 0

    def update(self):
        key = 0
        key = self.getch()
        return val = [0,0]
        if key == "w":
            val = self.forward()
        elif key == "s":
            val = self.back()
        elif key == "a":
            val = self.left()
        elif key == "d":
            val = self.right()
        return val

    def forward(self):
        return [-50, 50]

    def back(self):
        return [50, -50]

    def left(self):
        return [-50,-50]

    def right(self):
        return [50, 50]

    def getch(self):
        # found here: https://www.raspberrypi.org/forums/viewtopic.php?p=513526
        old_settings = termios.tcgetattr(0)
        new_settings = old_settings[:]
        #settings from: https://stackoverflow.com/questions/21791621/taking-input-from-sys-stdin-non-blocking
        new_settings[3] &= ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(0, termios.TCSANOW, new_settings)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(0, termios.TCSANOW, old_settings)

        return ch
