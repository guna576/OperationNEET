from vehicle import Vehicle
from Strategy.sports_drive_strategy import SportsDriveStrategy


class SportsVehicle(Vehicle):

    def __init__(self):
        super().__init__(SportsDriveStrategy())
        