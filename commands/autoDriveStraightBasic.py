


from wpilib.command.command import Command
from subsystems.driveBase import driveBase


class AutoDriveStraightBasic(Command):

    def __init__(self):
        super().__init__()
        self.requires(driveBase)
        self.finished = False
        
    def initialize(self):
        driveBase.drive(0.33, 0.33)
        self.finished = True
               
    def isFinished(self):
        return self.finished

    def end(self):
        self.finished = False