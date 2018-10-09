class Motor:
    """
    A class responsible for defining and controlling motors
    """

    def __init__(self, pigpio_object, motor_enable, motor_direction, pwm_range, pwm_freq):
        self.gpioPi = pigpioObject

        # set motor enable/direction to outputs
        self.gpioPi.set_mode(motor_enable, OUTPUT)
        self.gpioPi.set_mode(motor_direction, OUTPUT)

        # set PWM pulsewidth range from 0 to pwmRange
        self.gpioPi.set_PWM_range(motor_enable, pwm_range)
        self.gpioPi.set_PWM_range(motor_direction, pwm_range)

        # set PWM Freq
        self.gpioPi.set_PWM_frequency(motor_enable, pwm_freq)
        self.gpioPi.set_PWM_frequency(motor_direction, pwm_freq)

        # Control Variables
        self.motor_direction = motor_direction
        self.motor_enable = motor_direction

    def speed(self, signed_speed):
        if signed_speed >= 0:
            self.gpioPi.write(self.motor_direction, 1)
            self.gpioPi.set_PWM_dutycycle(self.motor_enable, signed_speed)
        else:
            self.gpioPi.write(self.motor_direction, 0)
            self.gpioPi.set_PWM_dutycycle(self.motor_enable, abs(signed_speed))
