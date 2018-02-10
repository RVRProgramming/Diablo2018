from pyfrc.physics.drivetrains import four_motor_drivetrain

from common import robotMap


class PhysicsEngine:
  
    def __init__(self, controller):
        self.controller = controller
        # self.controller.add_device_gyro_channel("NavX-MXP") # This is not working, so I commented it out for now. It doesn't break anything though.

    """
        Keyword arguments:
        hal_data -- Data about motors and other components.
        now -- Current time in milliseconds
        tm_diff -- Difference between current time and time when last checked
    """

    def update_sim(self, hal_data, now, tm_diff):

        # Simulate the drivetrain
        lf_motor = hal_data['CAN'][robotMap.left1]['value'] / 5
        lr_motor = hal_data['CAN'][robotMap.left2]['value'] / 5
        rf_motor = hal_data['CAN'][robotMap.right1]['value'] / 5
        rr_motor = hal_data['CAN'][robotMap.right2]['value'] / 5

        fwd, rcw = four_motor_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor, speed=10)

        self.controller.drive(fwd, rcw, tm_diff)
