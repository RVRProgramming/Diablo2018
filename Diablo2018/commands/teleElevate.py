from wpilib.command.command import Command

from common.oi import oi
from subsystems.elevator import elevator
from common import robotMap


class TeleElevate(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Elevator while running.
        self.requires(elevator)
        
    def execute(self):
        # Set Elevator speed.
        if abs(oi.getElevatorSpeed()) < robotMap.elevatorDeadzone:
            elevator.elevate(0)
        else:
            elevator.elevate(oi.getElevatorSpeed() * robotMap.elevatorMaxSpeed)
                  
    def isFinished(self):
        # TeleElevate never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop elevate motors.
        elevator.elevate(0)

