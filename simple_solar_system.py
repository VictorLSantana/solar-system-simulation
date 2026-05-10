
import turtle

from solar_system import SolarSystem, Sun


SUN_MASS = 10_000_000
SUN_SIZE = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 550


solar_system = SolarSystem(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

sun = Sun(solar_system=solar_system, mass=SUN_MASS, display_size=SUN_SIZE)

sun.draw()
turtle.done()

