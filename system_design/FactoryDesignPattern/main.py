from vehicle_factory import VehicleFactory

def main():
    vehicle_type = input("Enter the type of vehicle: ")
    vehicle = VehicleFactory()
    vehicle.createVehicle(vehicle_type)

main()