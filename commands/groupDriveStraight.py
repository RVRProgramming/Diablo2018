from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

import commands


class GroupDriveStraight(CommandGroup):
    
    def __init__(self):
        super().__init__()
        
        self.addSequential(commands.AutoDriveStraightBasic())
        self.addSequential(WaitCommand(4))
        self.addSequential(commands.DisaDisableTalons())