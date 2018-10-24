from wpilib.command.command import Command

from subsystems.driveBase import driveBase


class AutoTurn(Command):
    def __init__(self, angle):
        super().__init__()
        self.angle = angle
        
    def initialize(self):
        super().initialize()
        driveBase.resetGyroAngle()
        
    def execute(self):
        super().execute()
        if self.angle > 0:
            driveBase.drive(0.5, -0.5)
        else:
            driveBase.drive(-0.5, 0.5)
        
    def isFinished(self):
        super().isFinished()
        if ((driveBase.getGyroAngle() > self.angle and self.angle > 0) or (driveBase.getGyroAngle() < self.angle and self.angle < 0)):
            return True
        else:
            return False
        
    def end(self):
        super().end()
        driveBase.drive(0, 0)