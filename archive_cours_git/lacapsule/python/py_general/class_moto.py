class Moto: 
    pilot = ""
    speed = 0

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def change_pilot(self, pilot):
        self.pilot = pilot

    def set_speed(self, rate, duration):
        if self.pilot != "":
            self.speed = rate * duration

    def __repr__(self):
        return "Info Moto : Pilot {} / Brand ({}) / Speed ({}) ".format(self.pilot, self.brand, self.speed) # change this !
    

my_moto = Moto("kawa", "red")

print(my_moto)