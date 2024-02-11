from hcsr04 import HCSR04
import time
from machine import Pin, PWM, SoftI2C
from servo import Servo
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# ESP32
sensor = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=10000)
led_white =Pin(25,Pin.OUT)
led_blue = Pin(33,Pin.OUT)
led_green = Pin(32,Pin.OUT)
led_red = Pin(4,Pin.OUT) 
buzzer=Pin(2,Pin.OUT)
which_range=[True,True,True,True]
motor=Servo(pin=22)
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(13), sda=Pin(12), freq=10000)     #initializing the I2C method for ESP32
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


def rest_true(pos):
    for i in range(0,4):
        if i==pos:
            which_range[i]=False
        else:
            which_range[i]=True

def buzz_it(rank):
    buzzer.value(0)
    if rank==0:
        buzzer.value(1)
        rest_true(pos=0)
        
    elif rank==1:
        buzzer.value(0)
        time.sleep(1)
        for i in range(0,3):
            buzzer.value(1)
            time.sleep(1)
            buzzer.value(0)
            time.sleep(1)
            rest_true(pos=1)
    elif rank==2:
        buzzer.value(0)
        time.sleep(1)
        for i in range(0,2):
            buzzer.value(1)
            time.sleep(1)
            buzzer.value(0)
            time.sleep(1)
            rest_true(pos=2)
    elif rank==3:
        buzzer.value(0)
        time.sleep(1)
        for i in range(0,1):
            buzzer.value(1)
            time.sleep(1)
            buzzer.value(0)
            time.sleep(1)
            rest_true(pos=3)
        
while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep(1)
    if distance<=10 and which_range[0]==True:
        time.sleep(1)
        lcd.clear()
        time.sleep(1)
        lcd.putstr("range 1")
        time.sleep(1)
        motor.move(0)
        time.sleep(1)
        led_white.value(1)
        led_blue.value(1)
        led_green.value(1)
        led_red.value(1)
        time.sleep(1)
        buzz_it(0)
        time.sleep(1)
        
            
        #time.sleep(2)
    if distance<=20 and distance>10 and which_range[1]==True:
        time.sleep(1)
        lcd.clear()
        time.sleep(1)
        lcd.putstr("range 2")
        time.sleep(1)
        buzzer.value(0)
        motor.move(45)
        time.sleep(1)
        led_white.value(1)
        led_blue.value(1)
        led_green.value(1)
        led_red.value(0)
        time.sleep(1)
        buzz_it(1)
        time.sleep(1)
       
        #time.sleep(2)
    if distance<=30 and distance>20 and which_range[2]==True:
        time.sleep(1)
        lcd.clear()
        time.sleep(1)
        lcd.putstr("range 3")
        time.sleep(1)
        buzzer.value(0)
        motor.move(90)
        time.sleep(1)
        led_white.value(1)
        led_blue.value(1)
        led_green.value(0)
        led_red.value(0)
        time.sleep(1)
        buzz_it(2)
        time.sleep(1)
       

        #time.sleep(2)
    if distance<=40 and distance>30 and which_range[3]==True:
        time.sleep(1)
        lcd.clear()
        time.sleep(1)
        lcd.putstr("range 4")
        time.sleep(1)
        buzzer.value(0)
        motor.move(135)
        time.sleep(1)
        led_white.value(1)
        led_blue.value(0)
        led_green.value(0)
        led_red.value(0)
        time.sleep(1)
        buzz_it(3)
        time.sleep(1)
        
        #time.sleep(2)
    if distance>40:
        time.sleep(1)
        lcd.clear()
        time.sleep(1)
        lcd.putstr("out of range")
        time.sleep(1)
        motor.move(180)
        time.sleep(1)
        led_white.value(0)
        led_blue.value(0)
        led_green.value(0)
        led_red.value(0)
        for i in range(0,3):
            if which_range[i]==False:
                which_range[i]=True
        time.sleep(1)
        buzz_it(4)
        time.sleep(1)
        

    
