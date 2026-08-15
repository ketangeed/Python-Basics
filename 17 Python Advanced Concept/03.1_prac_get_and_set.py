# If it is a...      You write it like...     Why?
# Normal Method	      obj.dance()	          It's an action. It needs ()
# Getter(@property)	  obj.name	       It's a piece of info. No () needed.
# Setter	          obj.name = "New"	 You are changing a value. Use =

# self._volume (The Secret Room): This is the actual variable where the data is hidden. We only touch this inside the class.

# class Thermostat:
#     def __init__(self, temperature):
#         self._temperature = temperature

#     @property
#     def temp (self):
#         return f"{self._temperature} °C"
    
#     @temp.setter
#     def temp(self, value):
#         if value < 10 :
#             self._temperature = 10
#         elif value > 30 :
#             self._temperature = 30
#         else :
#             self._temperature = value

# ac = Thermostat(50)
# ac.temp = 25
# print(ac.temp)




# class Car :
#     def __init__(self, front_door):
#         self.front_door = front_door

#     @property
#     def front_door(self):
#         return f"{self._front_door}km/h"
    
#     @front_door.setter
#     def front_door(self, value):
#         if value > 160:
#             self._front_door = 160
#         else : 
#             self._front_door = value

# mycar = Car(200)
# print(mycar.front_door)




# class Sensor:
#     def log_change(func):
#         def wrapper (self, value):
#             print("LOG: Updating the system...")
#             return func(self, value)
#         return wrapper
    
#     def __init__(self, front_door):
#         self.temp = front_door


#     @property
#     def temp(self):
#         return f"{self._front_door}°C"
    
#     @temp.setter 
#     @log_change
#     def temp(self, value):
#         if value < -50 :
#             self._front_door = -50
#         else : 
#             self._front_door = value

# s1 = Sensor(25)
# print(s1.temp)

# s1.temp = -100
# print(s1.temp)

# s1.temp = 10
# print(s1.temp)




class Hero:
    def __init__(self, hp):
        self.__hp = hp

    @property
    def get_hp(self):
        return self.__hp
    
    @get_hp.setter
    def set_hp(self, new_hp):
        if new_hp < 0:
            self.__hp == 0
        else:
            new_hp = self.__hp
player = Hero(100)
player.set_hp = -50
print(player.get_hp())
