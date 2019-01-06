import sys, tty, termios, time

class WASD_control:
    """
    controls a chassis using input from the python terminal
    """
    #max time between key presses before it turns motor off


    def __init__(self, max_speed):
        #intial stuffs
        self._acceleration = 10
        self._deceleration = 25
        self._left_speed = 0
        self._right_speed = 0
        self._max_speed = max_speed
        self._current_time = 0
        self._previous_time = 0
        self._val = 0

    def update(self):
        key = self.getch()
        if key == "w":
            self._val = self.forward()
        elif key == "s":
            self._val = self.back()
        elif key == "a":
            self._val = self.left()
        elif key == "d":
            self._val = self.right()
        else:
            self._val = [0,0]
        return self._val

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
        #the termios.ECHO flag results in non blocking values
        new_settings[3] &= ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(0, termios.TCSANOW, new_settings)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(0, termios.TCSANOW, old_settings)

        return ch
