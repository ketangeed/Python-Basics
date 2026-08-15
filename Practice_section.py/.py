class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    def say_hello(self):
        print(f"Hello, my name is {self.name} and my battery is at {self.battery_level}%")

    def use_robot(self, amount):
        if amount > self.battery_level:
            print("Not enough battery.")
        else:
            self.battery_level -= amount  
            print(f"Used {amount} units. Battery is now {self.battery_level}%")
           

my_robot = Robot("Robo-1", 50) 
my_robot.use_robot(30)   
my_robot.say_hello()           