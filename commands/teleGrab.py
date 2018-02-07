from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.grabber import grabber


class TeleGrab(Command):

    def __init__(self):
        super().__init__()
        self.requires(grabber)
        
    def execute(self):
        if oi.getGrabberOpen() and not oi.getGrabberClose():
            grabber.grab(robotMap.grabberSpeed)
        elif oi.getGrabberClose() and not oi.getGrabberOpen():
            grabber.grab(-robotMap.grabberSpeed)
        else:
            grabber.grab(0)
                
    def isFinished(self):
        return False

    def interrupted(self):
        grabber.grab(0)

