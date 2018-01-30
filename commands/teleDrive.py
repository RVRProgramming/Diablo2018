from wpilib.command.command import Command

from common.oi import oi
from subsystems.driveBase import driveBase


class TeleDrive(Command):

    def __init__(self):
        super().__init__()
        self.requires(driveBase)
        
    def execute(self):
        driveBase.drive(oi.getLeftDrive() * oi.getSlowDrive(), oi.getRightDrive() * oi.getSlowDrive())
                
    def isFinished(self):
        return False

    def interrupted(self):
        driveBase.drive(0, 0)
