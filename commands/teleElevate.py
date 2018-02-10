from wpilib.command.command import Command

from common.oi import oi
from subsystems.elevator import elevator


class TeleElevate(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(elevator)
        
    def execute(self):
        # Set Elevator speed to the elevator joystick value
        elevator.elevate(oi.getElevatorSpeed())
                
    def isFinished(self):
        # TeleElevate never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop elevate motors.
        elevator.elevate(0)

