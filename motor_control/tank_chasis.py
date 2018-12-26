import Motor from motor
class TankChasis:
    """A class that creates and controls four motors"""
    def __init__(self, pigpioObject, motorPinsArray, pwmRange, pwmFreq):
        self.FrontLeftMotor = Motor(pigpioObject, motorPinsArray[0][0], motorPinArray[0][1], pwmRange, pwmFreq)
        self.BackLeftMotor = Motor(pigpioObject, motorPinArray[1][0], motorPinArray[1][1], pwmRange, pwmFreq)
        self.FrontRightMotor = Motor(pigpioObject, motorPinArray[2][0], motorPinArray[2][1], pwmRange, pwmFreq)
        self.BackRightMotor = Motor(pigpioObject, motorPinArray[3][0], motorPinArray[3][1], pwmRange, pwmFreq)
