
from wpilib.command.command import Command

from common import robotMap
from subsystems.driveBase import driveBase


class AutoDriveStraightPID(Command):
    
    def __init__(self, distance):
        super().__init__()
        self.distance = distance * robotMap.countsPerRevolution
        
    def initialize(self):
        super().initialize()
        driveBase.resetEncoderPosition()
        
    def execute(self):
        driveBase.positionPID(self.distance)
            
    def isFinished(self):
        # Return True if the velocity of both sides is less than 1 RPM.
        return True if abs((driveBase.getLeftVelocity() * 10) / robotMap.countsPerRevolution) * 60 < 1 and abs((driveBase.getRightVelocity() * 10) / robotMap.countsPerRevolution) * 60 < 1 else False
    
    def end(self):
        super().end()
        driveBase.drive(0, 0)

