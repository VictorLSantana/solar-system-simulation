
import math
import turtle

DISPLAY_SIZE = 20


class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen() 
        self.solar_system.tracer(0) # set delay of update drawing
        self.solar_system.setup(width, height) #size of the screen
        self.solar_system.bgcolor("black") # background color
        
        self.bodies = []
        
    def add_body(self, body):
        self.bodies.append(body)
        
    def remove_body(self, body):
        self.bodies.remove(body) 

class SolarSystemBody(turtle.Turtle):
    
    def __init__(self, solar_system, mass, display_size, position=(0, 0), velocity=(0, 0)):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = display_size
        
        self.penup()
        self.hideturtle()
        
        solar_system.add_body(self) #solar system that the body (self) belongs to
        
    def draw(self):
        self.dot(self.display_size)
        

class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass, display_size, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, display_size, position, velocity)
        self.color("yellow")





class Planet(SolarSystemBody):
    pass

