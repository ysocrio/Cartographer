#written for Python 3 running on Raspberry Pi
#turns on motors

#libraries used
import pigpio           #GPIO Daemon/library that controls GPIO (need to install/run the daemon first)
from time import sleep  #handles sleep

MyPi = pigpio.pi()  #create an instance of the pi class called MyPi, MyPi will represent our rapsberrypi

incrementDelay = .1     #unit is in seconds, delay between each increment/decrement
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

#for loop start cycles through each motor
  #for loop cycles up values
  #for loop cycles down values
#for loop end
