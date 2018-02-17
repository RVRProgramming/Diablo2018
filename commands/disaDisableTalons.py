from wpilib.command.command import Command
from subsystems.driveBase import driveBase


class DisaDisableTalons(Command):

    def __init__(self):
        super().__init__()
        self.requires(driveBase)
        self.finished = False
        
    def initialize(self):
        super().initialize()
        driveBase.disable()
        self.finished = True
               
    def isFinished(self):
        return self.finished

    def end(self):
        self.finished = False