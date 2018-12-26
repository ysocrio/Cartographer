#written for Python 3 running on Raspberry Pi
#turns on motors


#libraries used
import pigpio           #GPIO Daemon/library that controls GPIO (need to instal$
from time import sleep  #handles sleep

Mypi = pigpio.pi()  #create an instance of the pi class called MyPi, MyPi will $
incrementTime = 0.05 #five second ramp up time
Motor1LeftEn = 13       #Pin 33
Motor1LeftDir = 5       #Pin 29
Motor2LeftEn = 19       #Pin 35
Motor2LeftDir = 6       #Pin 31
Motor1RightEn = 26      #Pin 37
Motor1RightDir = 8      #Pin 24
Motor2RightEn = 25      #Pin 22
Motor2RightDir = 7      #Pin 26


#prompt for user input to start
userInput = raw_input("Press Enter To Start Test")

#set all pin modes
Mypi.set_mode(Motor1LeftEn, pigpio.OUTPUT)
Mypi.set_mode(Motor1LeftDir, pigpio.OUTPUT)
Mypi.set_mode(Motor2LeftEn, pigpio.OUTPUT)
Mypi.set_mode(Motor2LeftDir, pigpio.OUTPUT)
Mypi.set_mode(Motor1RightEn, pigpio.OUTPUT)
Mypi.set_mode(Motor1RightDir, pigpio.OUTPUT)
Mypi.set_mode(Motor2RightEn, pigpio.OUTPUT)
Mypi.set_mode(Motor2RightDir, pigpio.OUTPUT)

#sets range for pwm to 0-100
Mypi.set_PWM_range(Motor1LeftEn, 100)
Mypi.set_PWM_range(Motor2LeftEn, 100)
Mypi.set_PWM_range(Motor1RightEn, 100)
Mypi.set_PWM_range(Motor2RightEn, 100)

#set pwm frequency for the motors
Mypi.set_PWM_frequency(Motor1LeftEn,1000)
Mypi.set_PWM_frequency(Motor2LeftEn,1000)
Mypi.set_PWM_frequency(Motor1RightEn,1000)
Mypi.set_PWM_frequency(Motor2RightEn,1000)

#set all motor directions
Mypi.write(Motor1LeftDir,1) #one for forward, zero for reverse
Mypi.write(Motor2LeftDir,1)
Mypi.write(Motor1RightDir,1)
Mypi.write(Motor2RightDir,1)

#ramp up and down each motor one at a time
for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor1LeftEn,currentDuty)
  sleep(incrementTime)
for currentDuty in range(100, 0, -1):
  Mypi.set_PWM_dutycycle(Motor1LeftEn,currentDuty)
  print(currentDuty)
  sleep(incrementTime)

for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor2LeftEn,currentDuty)
  time.sleep(incrementTime)
for currentDuty in range(100, 0, -1):
  Mypi.set_PWM_dutycycle(Motor2LeftEn,currentDuty)
  time.sleep(incrementTime)

for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor1RightEn,currentDuty)
  time.sleep(incrementTime)
for currentDuty in range(100, 0, -1):
  Mypi.set_PWM_dutycycle(Motor1RightEn,currentDuty)
  time.sleep(incrementTime)

for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor2RightEn,currentDuty)
  time.sleep(incrementTime)
for currentDuty in range(100, 0, -1):
  Mypi.set_PWM_dutycycle(Motor2RightEn,currentDuty)
  time.sleep(incrementTime)

#release pi processes
Mypi.stop()
