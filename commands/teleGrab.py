from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.grabber import grabber


class TeleGrab(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(grabber)
        
    def execute(self):
        
        # Open grabber if open button is exclusively pressed.
        if oi.getGrabberOpen() and not oi.getGrabberClose():
            grabber.grab(robotMap.grabberSpeed)
        # Close grabber if close button is exclusively pressed.
        elif oi.getGrabberClose() and not oi.getGrabberOpen():
            grabber.grab(-robotMap.grabberSpeed)
        # Otherwise, set the Grabber to stop.
        else:
            grabber.grab(0)
                
    def isFinished(self):
        # TeleGrab never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop grab motors.
        grabber.grab(0)

