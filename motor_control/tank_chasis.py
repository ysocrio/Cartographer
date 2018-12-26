from motor import Motor
class TankChasis:
    """A class that creates and controls four motors"""
    def __init__(self, pigpioObject, motorPinsArray, pwmRange, pwmFreq):
        self.FrontLeftMotor = Motor(pigpioObject, motorPinsArray[0][0], motorPinsArray[0][1], pwmRange, pwmFreq)
        self.BackLeftMotor = Motor(pigpioObject, motorPinsArray[1][0], motorPinsArray[1][1], pwmRange, pwmFreq)
        self.FrontRightMotor = Motor(pigpioObject, motorPinsArray[2][0], motorPinsArray[2][1], pwmRange, pwmFreq)
        self.BackRightMotor = Motor(pigpioObject, motorPinsArray[3][0], motorPinsArray[3][1], pwmRange, pwmFreq)
