#!/usr/bin/env python
import Display,Webparser,sys
import time

print "hello :-)"
d = Display.Display()
print "end"
parse1 = Webparser.Webparser(sys.argv[1])
parse2 = Webparser.Webparser(sys.argv[2])
listnum1 =  parse1.getmaxprices()
listnum2 =  parse2.getmaxprices()

print "t" , listnum1[-1]


while True:
   d.drawList(listnum1,50,str(sys.argv[1] + " " + listnum1[-1] + "$"))
   time.sleep(5)
   d.drawList(listnum2,50,str(sys.argv[2] + " " + listnum2[-1] + "$"))
   time.sleep(5)

