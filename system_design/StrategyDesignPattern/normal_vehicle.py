from vehicle import Vehicle
from Strategy.normal_drive_strategy import NormalDriveStrategy

class NormalVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())