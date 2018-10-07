#written for Python 3 running on Raspberry Pi
#turns on motors

#start pigpio daemon
os.system("sudo pigpiod")

#libraries used
import pigpio           #GPIO Daemon/library that controls GPIO (need to install/run the daemon first)
from time import sleep  #handles sleep

MyPi = pigpio.pi()  #create an instance of the pi class called MyPi, MyPi will represent our rapsberrypi
incrementTime = 0.05 #five second ramp up time 
Motor1LeftEn = 12
Motor1LeftDir = 14
Motor2LeftEn = 13
Motor2LeftDir = 15
Motor1RightEn = 18
Motor1RightDir = 20
Motor2RightEn = 19
Motor2RightDir = 21

#prompt for user input to start
userInput = input("Press Enter To Start Test")

#set all pin modes
Mypi.set_mode(Motor1LeftEn, OUTPUT)
Mypi.set_mode(Motor1LeftDir, OUTPUT)
Mypi.set_mode(Motor2LeftEn, OUTPUT)
Mypi.set_mode(Motor2LeftDir, OUTPUT)
Mypi.set_mode(Motor1RightEn, OUTPUT)
Mypi.set_mode(Motor1RightDir, OUTPUT)
Mypi.set_mode(Motor2RightEn, OUTPUT)
Mypi.set_mode(Motor2RightDir, OUTPUT)

#sets range for pwm to 0-1000
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
  time.sleep(incrementTime)
for currentDuty in range(100, 0):
  Mypi.set_PWM_dutycycle(Motor1LeftEn,currentDuty)
  time.sleep(incrementTime)

for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor2LeftEn,currentDuty)
  time.sleep(incrementTime)
for currentDuty in range(100, 0):
  Mypi.set_PWM_dutycycle(Motor2LeftEn,currentDuty)
  time.sleep(incrementTime)

for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor1RightEn,currentDuty)
  time.sleep(incrementTime)
for currentDuty in range(100, 0):
  Mypi.set_PWM_dutycycle(Motor1RightEn,currentDuty)
  time.sleep(incrementTime)

for currentDuty in range(0, 100):
  Mypi.set_PWM_dutycycle(Motor2RightEn,currentDuty)
  time.sleep(incrementTime)
for currentDuty in range(100, 0):
  Mypi.set_PWM_dutycycle(Motor2RightEn,currentDuty)
  time.sleep(incrementTime)

#for loop start cycles through each motor
  #for loop cycles up values
  #for loop cycles down values
#for loop end

#release pi processes
Mypi.stop()
#stop the pigpio daemon
os.system("sudo killall pigpiod")
