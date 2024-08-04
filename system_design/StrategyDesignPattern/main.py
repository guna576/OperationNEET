from vehicle import Vehicle
from normal_vehicle import NormalDriveStrategy
from sports_vehicle import SportsDriveStrategy

def main():
    
    sports_obj: Vehicle = SportsDriveStrategy()
    normal_obj: Vehicle = NormalDriveStrategy()

    sports_obj.drive()
    normal_obj.drive()


main()