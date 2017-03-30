#!/usr/bin/env python
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
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
stockname = "NOK"
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()

disp.clear()
disp.display()


width = 128
height = 64
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
url = 'https://www.google.com/finance/historical?output=csv&q='+stockname
response = urllib2.urlopen(url)
cr = csv.reader(response)
csvlist = list(cr)
csvlist.pop(0)
max = csvlist[0][4]
min = max
for row in csvlist:
    if(row[4] > max):
        max = row[4]
    if(row[4]<min):
        min = row[4]
#print max , min
#print len(csvlist)
j=0
for i in range(len(csvlist)-128, len(csvlist)):
    y2= 64+16 - int(float(str(csvlist[i][4]))*64/(float(max) ))
    print int(j), 63,int(j),int(y2)
    draw.line((int(j), int(y2)-1,int(j),int(y2)),  fill=255)
#    draw.line((int(j), 63,int(j),int(y2)),  fill=255)
    j+=1

font = ImageFont.truetype('Minecraftia-Regular.ttf', 15)
current =  str(csvlist[len(csvlist)-1][4])
print current
draw.text((2, 40),  stockname+": "+current,  font=font, fill=1)

disp.image(image)
disp.display()

