from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.grabber import grabber


class TeleGrabBasic(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(grabber)
        
    def execute(self):
        if oi.getGrabberOpen():
            grabber.openSimple(-1)
            
        if oi.getGrabberClose():
            grabber.openSimple(1)
            
        if not oi.getGrabberClose() and not oi.getGrabberOpen():
            grabber.openSimple(0)
                
    def isFinished(self):
        # TeleGrab never finishes.
        return False