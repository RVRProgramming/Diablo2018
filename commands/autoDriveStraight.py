
from wpilib.command.command import Command
from wpilib.robotbase import RobotBase

from subsystems.driveBase import driveBase


class AutoDriveStraight(Command):
    
    def __init__(self, distance):
        super().__init__()
        self.distance = distance * 1000 if RobotBase.isSimulation() else distance * 4096
        
    def initialize(self):
        super().initialize()
        driveBase.resetEncoder()
        
    def execute(self):
        super().execute()
        if self.distance < 0:
            driveBase.drive(-0.5, -0.5)
        else:
            driveBase.drive(0.5, 0.5)
            
    def isFinished(self):
        super().isFinished()
        if ((driveBase.getLeftEncoder() > self.distance and driveBase.getRightEncoder() > self.distance and self.distance > 0) or (driveBase.getLeftEncoder() < self.distance and driveBase.getRightEncoder() < self.distance and self.distance < 0)):
            return True
        else:
            return False 
    
    def end(self):
        super().end()
        driveBase.drive(0, 0)

