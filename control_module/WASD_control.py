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
        return [-50, 50]

    def back(self):
        return [50, -50]

    def left(self):
        return [-50,-50]

    def right(self):
        return [50, 50]

    def getch(self):
        #update timekeeping variables
        self._current_time = time.clock()
        self._elapsed_time = self._current_time - self._previous_time
        print(self._elapsed_time)
        # found here: https://www.raspberrypi.org/forums/viewtopic.php?p=513526
        old_settings = termios.tcgetattr(0)
        new_settings = old_settings[:]
        new_settings[3] &= ~termios.ICANON
        try:
            termios.tcsetattr(0, termios.TCSANOW, new_settings)
            ch = sys.stdin.read(1)
            print("test")
            #update _previous_time
            self._previous_time = self._current_time
        finally:
            termios.tcsetattr(0, termios.TCSANOW, old_settings)

        #check to see that a key has not been pressed in the last _key_timeout seconds
        if self._elapsed_time >= self._key_timeout:
            ch = 0
        #if a key has been pressed in the last _key_timeout seconds, ch is the
        #pressed key, otherwise ch is zero
        return ch
