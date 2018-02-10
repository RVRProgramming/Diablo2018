import wpilib
from wpilib.command.subsystem import Subsystem

from common import robotMap


class Grabber(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors.
        self.leftArmMotor = wpilib.Spark(robotMap.leftArmMotor)
        self.rightArmMotor = wpilib.Spark(robotMap.rightArmMotor)
        
    def grab(self, speed):
        # Set grabbing speed.
        self.leftArmMotor.set(speed)
        self.rightArmMotor.set(speed)


grabber = Grabber()
