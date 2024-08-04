from bike import Bike
from car import Car
from vehicle import Vehicle


class VehicleFactory(Vehicle):
    my_vehicle: Vehicle = None
    @staticmethod
    def createVehicle(vehicle_type: str) -> None:
        if vehicle_type == "bike":
            VehicleFactory.my_vehicle: Vehicle =  Bike()
        elif vehicle_type == "car":
            VehicleFactory.my_vehicle: Vehicle = Car()
    
