
from wpilib.command.command import Command

from subsystems.driveBase import driveBase
from common import robotMap


class AutoDriveStraight(Command):
    
    def __init__(self, distance):
        super().__init__()
        self.distance = distance * robotMap.countsPerRevolution
        
    def initialize(self):
        super().initialize()
        driveBase.resetEncoderPosition()
        
    def execute(self):
        super().execute()
        if self.distance < 0:
            driveBase.drive(-0.35, -0.35)
        else:
            driveBase.drive(0.35, 0.35)
            
    def isFinished(self):
        super().isFinished()
        if ((driveBase.getLeftPosition() > self.distance and driveBase.getRightPosition() > self.distance and self.distance > 0) or (driveBase.getLeftPosition() < self.distance and driveBase.getRightPosition() < self.distance and self.distance < 0)):
            return True
        else:
            return False 
    
    def end(self):
        super().end()
        driveBase.drive(0, 0)

