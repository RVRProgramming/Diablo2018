from wpilib.command.command import Command

from common.oi import oi
from subsystems.grabber import grabber


class TeleGrab(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(grabber)
        
    def initialize(self):
        self.leftAmpTrigger = True
        self.rightAmpTrigger = True
        
    def execute(self):
        left = 0
        right = 0
        
        if oi.getGrabberClose() and not oi.getGrabberOpen():
            self.leftAmpTrigger = True
            self.rightAmpTrigger = True
            left = 1
            right = 1
        elif oi.getGrabberOpen() and not oi.getGrabberClose():
            left = -1 if grabber.getLeftCurrent() < 15 and self.leftAmpTrigger else 0
            right= -1 if grabber.getRightCurrent() < 15 and self.rightAmpTrigger else 0
            
            if grabber.getLeftCurrent() > 15:
                self.leftAmpTrigger = False
            
            if grabber.getRightCurrent() > 15:
                self.rightAmpTrigger = False
        else:
            left = 0
            right = 0
            
        grabber.grab(left, right)
                    
    def isFinished(self):
        return False
        