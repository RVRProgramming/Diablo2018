import time

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
        grabber.resetEncoders()
        self.position = 0
        self.lastTime = self.getCurrentTime()
        
    def execute(self):
        timeDiff = self.getCurrentTime() - self.lastTime
        self.lastTime = self.getCurrentTime()
        if (not oi.getGrabberOpen() and oi.getGrabberClose()) and (oi.getGrabberOpen() or oi.getGrabberClose()):
            if oi.getGrabberOpen():
                self.position += self.getPosAmount(timeDiff)
                self.position = robotMap.grabberMaxPosition if self.position > robotMap.grabberMaxPosition else self.position
            if oi.getGrabberClose():
                self.position -= self.getPosAmount(timeDiff)
                self.position = robotMap.grabberMinPosition if self.position < robotMap.grabberMinPosition else self.position
        else:
            pass
        
        leftError = self.position - grabber.getLeftEncoder()
        if leftError < 100:
            grabber.openLeft(0)
        elif leftError > robotMap.grabberMaxError:
            grabber.openLeft(robotMap.grabberSpeed)
        elif leftError > 100 and left

                
    def isFinished(self):
        # TeleGrab never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop grab motors.
        grabber.openSimple(0)

    def getCurrentTime(self):
        return int(time.time() * 1000)
    
    def getPosAmount(self, time):
        return (robotMap.grabberMaxPosition/robotMap.grabberOpenTime) * time
    