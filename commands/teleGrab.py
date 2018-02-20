from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.grabber import grabber


class TeleGrab(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(grabber)
        
    def initialize(self):
        grabber.startPID()
        self.position = 0
        
    def execute(self):
        if oi.getGrabberOpen() and self.position < robotMap.maxAccum:
            self.position += robotMap.accumSpeed
            
        if oi.getGrabberClose() and self.position > robotMap.minAccum:
            self.position -= robotMap.accumSpeed
            
        grabber.grab(self.position)
                
    def isFinished(self):
        # TeleGrab never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop grab motors.
        grabber.stopPID()

