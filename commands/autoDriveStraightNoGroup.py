
import time

from wpilib.command.command import Command

from subsystems.driveBase import driveBase


class AutoDriveStraightNoGroup(Command):

    def __init__(self):
        super().__init__()
        self.requires(driveBase)
        
    def initialize(self):
        self.startTime = int(time.time() * 1000)

    def execute(self):
        driveBase.drive(0.33, 0.33)
               
    def isFinished(self):
        if int(time.time() * 1000) - self.startTime > 5000:
            return True
        else:
            return False

    def end(self):
        driveBase.drive(0,0)