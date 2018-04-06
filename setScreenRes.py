import sys
import win32api
from pywintypes import DEVMODEType

resolution_list = [[1920,1080], [1680,1050], [1600,1024], [1600,900]]

depth = 32
success = -2
resItem = 0
attempts = 5

while success != 0 and attempts != 0:
    width = resolution_list[resItem][0]
    height = resolution_list[resItem][1]
    
    print("trying resolution ", width, " x ", height)
    
    mode1 = win32api.EnumDisplaySettings()
    mode1.PelsWidth = width
    mode1.PelsHeight = height
    mode1.BitsPerPel = depth

    success = win32api.ChangeDisplaySettings(mode1, 0)
    print(success)
    resItem += 1
    attempts -= 1
