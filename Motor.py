class Motor:
  """A class responsible for defining and controlling motors"""
  def __init__(self, pigpioObject, motorEnable, motorDirection, pwmRange, pwmFreq):
    self.gpioPi = pigpioObject
    #set motor enable/direction to outputs
    gpioPi.set_mode(motorEnable, OUTPUT)
    gpioPi.set_mode(motorDirection, OUTPUT)
    #set PWM pulsewidth range from 0 to pwmRange
    gpioPi.set_PWM_range(motorEnable, pwmRange)
    gpioPi.set_PWM_range(motorDirection, pwmRange)
    #set PWM Freq
    gpioPi.set_PWM_frequency(motorEnable, pwmFreq)
    gpioPi.set_PWM_frequency(motorDirection, pwmFreq)
  def speed(self, signedSpeed):
    if signedSpeed >= 0:
      gpioPi.write(motorDirection,1)
      gpioPi.set_PWM_dutycycle(motorEnable,signedSpeed)
    ele:
      gpioPi.write(motorDirection,0)
      gpioPi.set_PWM_dutycycle(motorEnable,abs(signedSpeed))
 class TankMix:
  """A class that creates and controls four motors"""
  def __init__(self, pigpioObject, motorArray, pwmRange, pwmFreq):
    FrontLeftMotor = Motor(pigpioObject, motorArray[1][1], motorArray[1][2], pwmRange, pwmFreq) 
    BackLeftMotor = Motor(pigpioObject, motorArray[2][1], motorArray[2][2], pwmRange, pwmFreq) 
    FrontRightMotor = Motor(pigpioObject, motorArray[3][1], motorArray[3][2], pwmRange, pwmFreq) 
    BackRightMotor = Motor(pigpioObject, motorArray[4][1], motorArray[4][2], pwmRange, pwmFreq)
