class car:
    def __init__(self,speed,fuel):
        self._speed=speed
        self._fuel=fuel

    def get_speed(self):
        return self._speed
    def set_speed(self,speed):
        if 0<=speed<=200:
            self._speed=speed
        else:
            print("invalid speed")
        
    def __fuel_effiency(self):
            return self._speed/10

    def __show_effiency(self):
            print("fuel efficiency:(self._fuel_efficiency()km/1)")

car1=car(100,50)
car1.show_efficiency()
car1.set_speed(145)
car1.show_efficiency()
car1.set_speed(200)
print("fuel level",car1._fuel_level)
