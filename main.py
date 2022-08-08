import machine
from machine import Pin
import time
pins = [Pin(15,Pin.OUT), Pin(13,Pin.OUT), Pin(12,Pin.OUT), Pin(14,Pin.OUT)]
switch = Pin(4,Pin.IN, Pin.PULL_UP)
speed = 220/100000.0

steps_to_top = 8500
 
def SteperStop():
    SteperWriteData([0,0,0,0])
    
def SteperWriteData(step_order):
    for i in range(0,4):
        pins[i].value(step_order[i])
        

def check_switch():
    if switch.value() == 0:
        return True
    return False

def SteperFrontTurn():
    global speed
    SteperWriteData([1,1,0,0])
    time.sleep(speed)
 
    SteperWriteData([0,1,1,0])
    time.sleep(speed)
 
    SteperWriteData([0,0,1,1])
    time.sleep(speed)
     
    SteperWriteData([1,0,0,1])   
    time.sleep(speed)
    
def SteperBackTurn():
    global speed
    SteperWriteData([1,1,0,0])
    time.sleep(speed)
     
    SteperWriteData([1,0,0,1])   
    time.sleep(speed)
     
    SteperWriteData([0,0,1,1])
    time.sleep(speed)
 
    SteperWriteData([0,1,1,0])
    time.sleep(speed)

def find_bottom():
    while True:
        SteperFrontTurn()
        if check_switch():
            return

def step_up():
    for i in range(0,100):
        SteperBackTurn()

def goto_top():
    for i in range(0,steps_to_top):
        SteperBackTurn()


step_up()
find_bottom()
goto_top()
        

