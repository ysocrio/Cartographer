import pigpio

class Motor:
    """
    A class responsible for defining and controlling motors
    """

    def __init__(self, pigpio_object, motor_enable, motor_direction, pwm_range, pwm_freq):
        # Sets up private versions of variables
        # Pigpio Object
        self._gpio_pi = pigpio_object
        self.update_gpio_pi(pigpio_object, motor_enable, motor_direction, pwm_range, pwm_freq)

        # Control Variables initialization. NOTE: any further assignments should be done through property setters
        # i.e, self.motor_direction / self.motor_enable calls.
        self._motor_direction = motor_direction
        self._motor_enable = motor_enable


# Property decorators for public variables.

    @property
    def gpio_pi(self):
        return self._gpio_pi

    @gpio_pi.setter
    # Throws an exception if  null gpio pi is received.
    def gpio_pi(self, new_gpio_pi):
        if not new_gpio_pi:
            raise Exception("motor.py, gpio_pi.setter(): Null new_gpio_pi received. Can't do that!\n")
        else:
            self._gpio_pi = new_gpio_pi

    @property
    def motor_direction(self):
        return self._motor_direction

    @motor_direction.setter
    # Simple setter. Can add initial value checking here if needed.
    def motor_direction(self, new_motor_direction):
        self._motor_direction = new_motor_direction

    @property
    def motor_enable(self):
        return self._motor_enable

    @motor_enable.setter
    # Simple setter. Can add initial value checking here if needed.
    def motor_enable(self, do_motor_enable):
        self._motor_enable = do_motor_enable

# End property decorators

    # Sets all gpio_pi parameters. Throws exception if gpio_pi is not yet assigned.
    def update_gpio_pi(self, motor_enable, motor_direction, pwm_range, pwm_freq):
        if not self._gpio_pi:
            raise Exception("motor.py, gpio_pi_initialization(): initialization cannot be run with null gpio_pi\n")
        else:
            # set motor enable/direction to outputs
            self._gpio_pi.set_mode(motor_enable, pigpio.OUTPUT)
            self._gpio_pi.set_mode(motor_direction, pigpio.OUTPUT)

            # set PWM pulsewidth range from 0 to pwmRange
            self._gpio_pi.set_PWM_range(motor_enable, pwm_range)
            self._gpio_pi.set_PWM_range(motor_direction, pwm_range)

            # set PWM Freq
            self._gpio_pi.set_PWM_frequency(motor_enable, pwm_freq)
            self._gpio_pi.set_PWM_frequency(motor_direction, pwm_freq)

    def speed(self, signed_speed):
        if signed_speed >= 0:
            self._gpio_pi.write(self.motor_direction, 1)
            self._gpio_pi.set_PWM_dutycycle(motor_enable, signed_speed)
        else:
            self._gpio_pi.write(self.motor_direction, 0)
            self._gpio_pi.set_PWM_dutycycle(motor_enable, abs(signed_speed))
