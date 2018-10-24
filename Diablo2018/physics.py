from pyfrc.physics.drivetrains import four_motor_drivetrain

from common import robotMap


class PhysicsEngine:

    def __init__(self, controller):
        # Initialize the Sim and Gyro.
        self.controller = controller
        self.controller.add_device_gyro_channel('navxmxp_spi_4_angle')        
        
    """
        Keyword arguments:
        hal_data -- Data about motors and other components.
        now -- Current time in milliseconds
        tm_diff -- Difference between current time and time when last checked
    """

    def update_sim(self, hal_data, now, tm_diff):

        # Simulate the drivetrain motors.
        lf_motor = hal_data['CAN'][robotMap.left1]['value'] / -5
        lr_motor = hal_data['CAN'][robotMap.left2]['value'] / -5
        rf_motor = hal_data['CAN'][robotMap.right1]['value'] / 5
        rr_motor = hal_data['CAN'][robotMap.right2]['value'] / 5

        # Simulate movement.
        speed, rotation = four_motor_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor, speed=10)
        self.controller.drive(speed, rotation, tm_diff)

        # Simulate encoders (NOTE: These values have not been calibrated yet.)
        hal_data['CAN'][robotMap.left1]['quad_position'] -= int(lf_motor * robotMap.countsPerRevolution)
        hal_data['CAN'][robotMap.right1]['quad_position'] += int(rf_motor * robotMap.countsPerRevolution)
