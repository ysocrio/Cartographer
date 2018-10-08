class Motor:
  """A class responsible for defining and controlling motors"""
  def __init__(self, pigpioObject, motorEnable, motorDirection, pwmRange, pwmFreq):
    gpioPi = pigpioObject
    #set motor enable/direction to outputs
    gpioPi.set_mode(motorEnable, OUTPUT)
    gpioPi.set_mode(motorDirection, OUTPUT)
    #set PWM pulsewidth range from 0 to pwmRange
    gpioPi.set_PWM_range(motorEnable, pwmRange)
    gpioPi.set_PWM_range(motorDirection, pwmRange)
    #set PWM Freq
    gpioPi.set_PWM_frequency(motorEnable, pwmFreq)
    gpioPi.set_PWM_frequency(motorDirection, pwmFreq)
