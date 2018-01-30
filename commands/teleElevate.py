from wpilib.command.command import Command

from common.oi import oi
from subsystems.elevator import elevator


class TeleElevate(Command):

    def __init__(self):
        super().__init__()
        self.requires(elevator)
        
    def execute(self):
        elevator.elevate(oi.getElevatorSpeed)
                
    def isFinished(self):
        return False

    def interrupted(self):
        elevator.elevate(0)

