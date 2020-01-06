### Sample python code for NeoPixels on Raspberry Pi
### this code is random suggestion from my family, friends, and other examples on the web. 
### orginal code: https://github.com/DanStach/rpi-ws2811
import time
import board
import neopixel
import random
import math
import serial
import ctypes
from neopixeleffects import NeopixelEffects


# param ~microcontroller.Pin pin: The pin to output neopixel data on.
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
# param int n: The number of neopixels in the chain
num_pixels = 144
#param int bpp: Bytes per pixel. 3 for RGB and 4 for RGBW pixels.
pixel_bpp = 3
#param float brightness: Brightness of the pixels between 0.0 and 1.0 where 1.0 is full brightness
pixel_brightness = 0.2
#param bool auto_write: True if the neopixels should immediately change when set. 
#                       If False, `show` must be called explicitly.
pixel_auto_write = False
#param tuple pixel_order: Set the pixel color channel order. GRBW is set by default.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)
#pixels = neopixel.NeoPixel(pin=pixel_pin, num_pixels, brightness=pixel_brightness, 
#                            auto_write=pixel_auto_write, pixel_order=ORDER)


effect = NeopixelEffects(pixels)

while True:
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(3)

    
    
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)

    print(len(pixels))
    print(pixels)
    #effect.rainbow_cycle(.001)    # rainbow cycle with 1ms delay per step
