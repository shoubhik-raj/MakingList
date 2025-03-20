# Write your code here :-)


from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(4),16)

np[0] = (255,0,0)
np[12] = (0,0,255)
np[10] = (0,255,0)
np.write()
