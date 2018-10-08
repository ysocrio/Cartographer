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
  def Speed(self, signedSpeed):
    if signedSpeed >= 0:
      gpioPi.write(motorDirection,1)
      gpioPi.set_PWM_dutycycle(motorEnable,signedSpeed)
    ele:
      gpioPi.write(motorDirection,0)
      gpioPi.set_PWM_dutycycle(motorEnable,abs(signedSpeed))
 class TankChasis:
  """A class that creates and controls four motors"""
  def __init__(self, pigpioObject, motorPinsArray, pwmRange, pwmFreq):
    self.FrontLeftMotor = Motor(pigpioObject, motorArray[0][0], motorArray[0][1], pwmRange, pwmFreq) 
    self.BackLeftMotor = Motor(pigpioObject, motorArray[1][0], motorArray[1][1], pwmRange, pwmFreq) 
    self.FrontRightMotor = Motor(pigpioObject, motorArray[2][0], motorArray[2][1], pwmRange, pwmFreq) 
    self.BackRightMotor = Motor(pigpioObject, motorArray[3][0], motorArray[3][1], pwmRange, pwmFreq)
    
