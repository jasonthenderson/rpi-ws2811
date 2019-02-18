### Sample python code for NeoPixels on Raspberry Pi
### this code is ported from Arduino NeoPixels effects in C++, from tweaking4all
### Arduino Controlled Tree - http://youtu.be/MD3-YBaFQvw
### orginal code: https://pastebin.com/Qe0Jttme


import time
import board
import neopixel
import random
import math
import serial
import ctypes



# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
wait_time = 1
thisbright = 255



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def wheelBrightLevel(pos, bright):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)

    # bight level logic
    color = brightnessRGB(r, g, b, bright)
    r = color[0]
    g = color[1]
    b = color[2]

    return color if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def brightnessRGB(red, green, blue, bright):
    r = (bright/256.0)*red
    g = (bright/256.0)*green
    b = (bright/256.0)*blue
    return (int(r), int(g), int(b))

def hsv_to_rgb(h, s, v):
    if s == 0.0: 
        v*=255
        return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i
    p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f))))
    v*=255
    i%=6
    if i == 0: 
        return (v, t, p)
    if i == 1: 
        return (q, v, p)
    if i == 2: 
        return (p, v, t)
    if i == 3: 
        return (p, q, v)
    if i == 4: 
        return (t, p, v)
    if i == 5: 
        return (v, p, q)

def random_burst(delayStart, delayEnd , LoopCount):
    for loop in range(LoopCount):
        randomIndex= random.randint(0, num_pixels-1)
        randomhue = random.randint(0, 255)
        randombright = random.randint(10, thisbright)
        
        # CHSV(rndhue, thissat, rndbright)
        #print(str(randomIndex) + " " + str(rndhue) + " " + str(rndbright))
        pixels[randomIndex] = wheelBrightLevel(randomhue, randombright)
        
        pixels.show()
        delay = random.randint(delayStart*1000, delayEnd*1000)/1000
        time.sleep(delay)

def colorAllPalette(palette):
    pNum = palette.count() # get number of colors in palette

    # set color of each pixel
    for i in range(num_pixels):
        index = (i % pNum)
        pixels[i] = palette[index]

    pixels.show()

def colorAll2Color(c1, c2):
    for i in range(num_pixels):
        if(i % 2 == 0): # even
            pixels[i] = c1
        else: # odd   
            pixels[i] = c2
    pixels.show()


 
def random_march(delay, cycles):
    for loop in range(cycles):

        for idex in range(num_pixels-1):
            ### previous logic that was not used...
            #if idex > 0: #if not last pixel
            #    r = idex - 1
            #else: # if last pixel
            #    r = num_pixels - 1

            # shift pixel value to previous pixel (pixel1 = value of pixel2,... and so on)
            pixels[idex] = pixels[idex+1]

        # change color of the last pixel
        pixels[num_pixels-1] = wheelBrightLevel(random.randint(0, 255), 255)

        # show pixel values
        pixels.show()
        time.sleep(delay)

def rotate_pixels(dirrection, delay, cycles):
    for loop in range(cycles):
        if dirrection > 0:
            startNum = 0 
            endNum = num_pixels-1
            pixelSave = pixels[0]
        else:
            startNum = num_pixels-1 
            endNum = 0
            pixelSave = pixels[num_pixels-1]
          
        for idex in range(startNum, endNum, dirrection):
            # shift pixel value to previous pixel (pixel1 = value of pixel2,... and so on)
            pixels[idex] = pixels[idex+1]

        if dirrection > 0:
            # change color of the last pixel
            pixels[num_pixels-1] = pixelSave
        else:
            # change color of the first pixel
            pixels[0] = pixelSave

        # show pixel values
        pixels.show()
        time.sleep(delay)



while True:
    random.seed(num_pixels)

    # make all pixels Red
    # fill(red, green, blue)
    pixels.fill((255, 0, 0)) # red
    pixels.show()
    time.sleep(wait_time)

    # make all pixels Green
    # fill(red, green, blue)
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(wait_time)

    # make all pixels Blue
    # fill(red, green, blue)
    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(wait_time)

    # shows 2 color every other pixel (red, green)
    # colorAll2Color((red1, green1, blue1), (red2, green2, blue2)) 
    colorAll2Color((255, 0, 0), (0, 255, 0)) 
    time.sleep(wait_time)

    # shows colors in color palette
    # colorAllPalette(palette): 
    sky_palette= ( (32,99,165), (47,157,226), (44,142,209), (152,191,222), (148,164,196) )
    colorAllPalette(sky_palette)
    time.sleep(wait_time)

    # makes the strand of pixels show 
    # rotate_pixels(dirrection, delay, cycles)
    rotate_pixels(1, .1, 100)
    time.sleep(wait_time)


    ### FixMe: think random_march and matrix are the same
    # makes the strand of pixels show random_march
    # random_march( delay, cycles)
    random_march(0.25, 256) 
    time.sleep(wait_time)


