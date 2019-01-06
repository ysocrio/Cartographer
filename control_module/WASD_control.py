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
        self._previous_keypress_time = 0
        self._keypress_timeout = .2
        self._val = [0,0]
        #prompt user about changing keyboard settings
        print("change keyboard settings to have a short repeat delay")
        print("on windows go to control panel -> keyboard -> repeat delay")

#run once per loop to calculate left and right motor speeds at any instance
    def update(self):
        #get the current key pressed, zero if no key is pressed
        key = self.getch()
        #calculate change of time from previous loop
        self._previous_time = self._current_time
        self._current_time = time.time()
        elapsed_time = self._current_time - self._previous_time
        #calculate
        time_since_last_keypress = self._current_time - self._previous_keypress_time
        #check to see if it is a movement keypress
        key_is_movement = ((key == "w")|(key == "a")|(key == "s")|(key == "d"))
        #if it is, record the time it accured then output to motors
        if key_is_movement:
            self._previous_keypress_time = self._current_time
            if key == "w":
                self._val = self.forward()
            elif key == "s":
                self._val = self.back()
            elif key == "a":
                self._val = self.left()
            elif key == "d":
                self._val = self.right()
        elif time_since_last_keypress >= self._keypress_timeout:
            self._val = [0,0]
        return self._val

#functions that run for each selected direction
    def forward(self):
        return [-50, 50]

    def back(self):
        return [50, -50]

    def left(self):
        return [-50,-50]

    def right(self):
        return [50, 50]

#function that returns a single character, unlike normal getch, this function
#is nonblocking and returns 0 if there is no input at that time
    def getch(self):
        # found here: https://www.raspberrypi.org/forums/viewtopic.php?p=513526
        old_settings = termios.tcgetattr(0)
        new_settings = old_settings[:]
        #settings from: https://stackoverflow.com/questions/21791621/taking-input-from-sys-stdin-non-blocking
        #the termios.ECHO flag results in non blocking values
        new_settings[3] &= (~termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(0, termios.TCSANOW, new_settings)
            ch = sys.stdin.read(1)
            print(ch)
        finally:
            termios.tcsetattr(0, termios.TCSANOW, old_settings)

        return ch
