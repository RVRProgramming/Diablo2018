from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.grabber import grabber


class TeleGrabBasic(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(grabber)
        
    def initialize(self):
        grabber.resetEncoders()
        self.stopToggle = False
        
    def execute(self):
        if oi.getGrabberOpen():
            grabber.openSimple(1)
            
        if oi.getGrabberClose():
            grabber.openSimple(-1)
            
        if not oi.getGrabberClose() and not oi.getGrabberOpen():
            grabber.openSimple(0)
                
    def isFinished(self):
        if not oi.getGrabberOverride:
            self.stopToggle = True
            
        if self.stopToggle: 
            return oi.getGrabberOverride()
        else:
            return False
    
    def end(self):
        robotMap.grabberMode = 0
        
    