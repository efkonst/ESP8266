import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import urllib2
import json,sys,csv
import datetime 
from datetime import timedelta
# Raspberry Pi pin configuration:

class Display:
        def __init__(self):
                print "initializing"
                self.width = 128
                self.height = 64
                self.RST = 24
                self.DC = 23
                self.SPI_PORT = 0
                self.SPI_DEVICE = 0
                self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=self.RST)
                print "initialized"

        def printR(self):
                self.disp.begin()
                self.disp.clear()
                self.disp.display()
                image = Image.new('1', (self.width, self.height))
                draw = ImageDraw.Draw(image)
                draw.rectangle((0,0,self.width,self.height), outline=0, fill=1)
                self.disp.image(image)
                self.disp.display()

        def createLines(self):
            image = Image.new('1', (self.width, self.height))
            draw = ImageDraw.Draw(image)
            for i in range(1,self.height,2):
                draw.line((0, i, self.width, i), fill=0)
            return image
        
        def printImage(self,img):
            self.disp.begin()
            self.disp.clear()
            self.disp.display()
            self.disp.image(img)
            self.disp.display()

