# Chris Smith
# Chapter 15 – CPX Part 1
# 07/15/2025

from adafruit_circuitplayground import cp
import time

class Region:
    def __init__(self, color, leds):
        self.__color = color          # (R, G, B)
        self.__leds = leds            # Tuple

    def set_color(self, color):
        self.__color = color

    def set_leds(self, leds):
        self.__leds = leds

    def get_color(self):
        return self.__color

    def get_leds(self):
        return self.__leds

    def all_on(self):
        for i in self.__leds:
            cp.pixels[i] = self.__color

    def all_off(self):
        for i in self.__leds:
            cp.pixels[i] = (0, 0, 0)

# Create regions
yellow = Region((255, 255, 0), (5, 6, 7))
blue = Region((0, 0, 255), (2, 3, 4))

# Flash regions
while True:
    yellow.all_on()
    blue.all_off()
    time.sleep(0.5)
    yellow.all_off()
    blue.all_on()
    time.sleep(0.5)


