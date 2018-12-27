
import pigpio
from time import sleep
import motor_control.tank_chasis as Robot
import motor_control.config as motor_config

MyPi = pigpio.pi() #create an instance of the pi class called MyPi
Chasis = Robot.TankChasis(MyPi, motor_config.List_Of_Pins, motor_config.PWM_Range, motor_config.PWM_Frequency)
pin = 17
conversion = 374.325

def Encode_Func(gpio, level, tick):
    Encode_Func.step += 1
Encode_Func.step = 0

MyPi.callback(pin,pigpio.RISING_EDGE,Encode_Func)

Chasis.FrontLeftMotor.speed(100)
Chasis.FrontRightMotor.speed(-100)
Chasis.BackLeftMotor.speed(100)
Chasis.BackRightMotor.speed(-100)
sleep(1)

Chasis.FrontLeftMotor.speed(0)
Chasis.FrontRightMotor.speed(0)
Chasis.BackLeftMotor.speed(0)
Chasis.BackRightMotor.speed(0)
sleep(1)
rot = conversion*Encode_Func.step
print(rot)

Chasis.FrontLeftMotor.speed(-100)
Chasis.FrontRightMotor.speed(100)
Chasis.BackLeftMotor.speed(-100)
Chasis.BackRightMotor.speed(100)
sleep(1)

Chasis.FrontLeftMotor.speed(0)
Chasis.FrontRightMotor.speed(0)
Chasis.BackLeftMotor.speed(0)
Chasis.BackRightMotor.speed(0)
rot = conversion*Encode_Func.step
print(rot)
