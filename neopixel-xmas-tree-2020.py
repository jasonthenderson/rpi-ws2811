### Sample python code for NeoPixels on Raspberry Pi
### this code is random suggestion from my family, friends, and other examples on the web. 
### orginal code: https://github.com/DanStach/rpi-ws2811
import time
#import board
#import neopixel
#import random
#import math
#import serial
#import ctypes
from neopixel_effects import NeopixelEffects


#param ~microcontroller.Pin pin: The pin to output neopixel data on.
#param int n: The number of neopixels in the chain
#param int bpp: Bytes per pixel. 3 for RGB and 4 for RGBW pixels.
#param float brightness: Brightness of the pixels between 0.0 and 1.0 where 1.0 is full brightness
#param bool auto_write: True if the neopixels should immediately change when set. 
#                       If False, `show` must be called explicitly.
#param tuple pixel_order: Set the pixel color channel order. GRBW is set by default.

rocket = NeopixelEffects()
print("The rocket is at (%d, %d)." % (rocket.x, rocket.y))