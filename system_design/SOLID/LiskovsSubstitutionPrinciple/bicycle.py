from non_engine_vehicle import NonEngineVehicle

class Bicycle(NonEngineVehicle):

    def apply_manual_energy(self):
        print("apply manual energy for bicycle")

    def honk(self):
        return super().honk()
    
    def apply_brakes(self):
        return super().apply_brakes()