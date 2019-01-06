#Top Level
if __name__ == '__main__':
    # TODO: Launch control, motor, sensor modules.
    import pigpio
    import control_module.WASD_control as control
    import motor_control.tank_chasis as chasis
    import motor_control.config as motor_config

    MyPi = pigpio.pi() #create an instance of the pi class called MyPi
    controller = control.WASD_control()
    robot = chasis.TankChasis(MyPi, motor_config.List_Of_Pins, motor_config.PWM_Range, motor_config.PWM_Frequency)

    while(1):
            [left_speed, right_speed] = controller.update()
            print(left_speed," ", right_speed)
            robot.FrontLeftMotor.speed(left_speed)
            robot.FrontRightMotor.speed(right_speed)
            robot.BackLeftMotor.speed(left_speed)
            robot.BackRightMotor.speed(right_speed)
