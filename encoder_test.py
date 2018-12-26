
import pigpio
import motor_control.tank_chasis as Robot
import motor_control.config as motor_config

MyPi = pigpio.pi() #create an instance of the pi class called MyPi
Chasis = Robot.TankChasis(MyPi, motor_config.List_Of_Pins, motor_config.PWM_Range, motor_config.PWM_Frequency)
