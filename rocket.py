import time

class Engine:
    max_fuel = 1000
    max_power = 100

    def __init__(self):
        self.engineON = False
        self.fuel = 0
        self.power = 0
        self.is_launched = False
        self.landOK = False

    def start_motor(self):
        self.engineON = True
        return self.engineON
    
    def stop_engine(self):
        self.engineON = False
        return self.engineON

    def check_fuel(self):
        print(self.fuel)

    def fill_fuel(self):
        if self.fuel <= self.max_fuel:
            self.fuel = self.max_fuel

    def launch(self):
        if self.engineON and self.fuel > (self.max_fuel / 2):
            self.fuel -= 300
            self.power = 80
            self.is_launched = True
        elif not self.engineON:
            self.is_launched = False
            print("Can't launch because the engine is off!!")
        elif self.fuel < (self.max_fuel / 2):
            self.is_launched = False
            print("You need to fill more fuel")
        return self.is_launched
   
class Rocket:
    def __init__(self):
        self.engine = Engine()
    
    def start_engine(self):
        self.engine.start_motor()

    def stop_engine(self):
        self.engine.stop_engine()
    
    def fill_fuel(self):
        self.engine.fill_fuel()
    
    def launch(self):
        if not self.engine.launch():
            print("Launch failed")
        else:
            print("Countdown begins")
            for i in range(10, 0, -1):
                print(i)
                time.sleep(0.1)
            print("Launch successful")



rocket = Rocket()
rocket.start_engine()
rocket.fill_fuel()
rocket.launch()

