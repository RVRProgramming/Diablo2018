
from wpilib.command.command import Command
from wpilib.robotbase import RobotBase

from subsystems.driveBase import driveBase


class AutoDriveStraight(Command):
    
    def __init__(self, distance):
        super().__init__()
        self.distance = distance * 1000 if RobotBase.isSimulation() else distance * 4096
        
    def initialize(self):
        super().initialize()
        driveBase.resetEncoderPosition()
        
    def execute(self):
        driveBase.positionPID(self.distance)
        driveBase.diagnosticsToSmartDash()
            
    def isFinished(self):
        return True if (abs((driveBase.getRightVelocity() + driveBase.getLeftVelocity())) / 8192) * 600 < 1 else False
    
    def end(self):
        super().end()
        driveBase.drive(0, 0)

