from wpilib.command.command import Command

from common.oi import oi
from subsystems.elevator import elevator
from common import robotMap


class TeleElevate(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Elevator while running.
        self.requires(elevator)
        
    def initialize(self):
        elevator.resetEncoder()
        
    def execute(self):
        # Set Elevator speed
        if oi.getElevatorSpeed() > 0 and elevator.getPosition() < robotMap.elevatorMaxHeight:
            elevator.elevate(oi.getElevatorSpeed())
        elif oi.getElevatorSpeed() < 0 and elevator.getPosition() > robotMap.elevatorMinHeight:
            elevator.elevate(oi.getElevatorSpeed())
        elif oi.getElevatorOverride():
            elevator.elevate(oi.getElevatorSpeed())
        else:
            elevator.elevate(0)
                  
    def isFinished(self):
        # TeleElevate never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop elevate motors.
        elevator.elevate(0)

