import time
import config
import traceback
import RPi.GPIO as GPIO
import time
import subprocess
import SH1106
from PIL import Image,ImageDraw,ImageFont

#GPIO define
RST_PIN        = 25
CS_PIN         = 8
DC_PIN         = 24

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13

KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16


GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up

prev_up_state = GPIO.input(KEY_UP_PIN)
up_count = 0
prev_left_state = GPIO.input(KEY_LEFT_PIN)
left_count = 0
prev_right_state = GPIO.input(KEY_RIGHT_PIN)
right_count = 0
prev_down_state = GPIO.input(KEY_DOWN_PIN)
down_count = 0
prev_center_state = GPIO.input(KEY_PRESS_PIN)
press_count = 0
prev_key1_state = GPIO.input(KEY1_PIN)
key1_count = 0
prev_key2_state = GPIO.input(KEY2_PIN)
key2_count = 0
prev_key3_state = GPIO.input(KEY3_PIN)
key3_count = 0

def clear():
    disp = SH1106.SH1106()
    disp.Init()
    disp.clear()
    
disp = SH1106.SH1106()
disp.Init()
disp.clear()
Himage2 = Image.new('1', (disp.width, disp.height), 255)        # 255: clear the frame
bmp = Image.open('pic.bmp')
Himage2.paste(bmp, (0,5))
Himage2=Himage2.rotate(0) 	
disp.ShowImage(disp.getbuffer(Himage2))

while 1:
    #Up
    curr_up_state = GPIO.input(KEY_UP_PIN)
    if prev_up_state == 1 and curr_up_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动Up按钮代码")
        else:
            print("关闭Up按钮代码")
    prev_up_state = curr_up_state
    #Left
    curr_left_state = GPIO.input(KEY_LEFT_PIN)
    if prev_left_state == 1 and curr_left_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动Left按钮代码")
        else:
            print("关闭Left按钮代码")
    prev_left_state = curr_left_state
    #Right
    curr_right_state = GPIO.input(KEY_RIGHT_PIN)
    if prev_right_state == 1 and curr_right_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动Right按钮代码")
        else:
            print("关闭Right按钮代码")
    prev_right_state = curr_right_state
    #Down
    curr_down_state = GPIO.input(KEY_DOWN_PIN)
    if prev_down_state == 1 and curr_down_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动Down按钮代码")
        else:
            print("关闭Down按钮代码")
    prev_down_state = curr_down_state
    #Center    
    curr_center_state = GPIO.input(KEY_PRESS_PIN)
    if prev_center_state == 1 and curr_center_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动Center按钮代码")
            opened_process = subprocess.Popen(['/usr/bin/python3', 'state.py'])
        else:
            print("关闭Center按钮代码")
            opened_process.terminate()
            clear()
    prev_center_state = curr_center_state
        
    #KEY1
    curr_key1_state = GPIO.input(KEY1_PIN)
    if prev_key1_state == 1 and curr_key1_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动key1按钮代码")
        else:
            print("关闭key1按钮代码")
    prev_key1_state = curr_key1_state
    #KEY2
    curr_key2_state = GPIO.input(KEY2_PIN)
    if prev_key2_state == 1 and curr_key2_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动key2按钮代码")
        else:
            print("关闭key2按钮代码")
    prev_key2_state = curr_key2_state
    #KEY3
    curr_key3_state = GPIO.input(KEY3_PIN)
    if prev_key3_state == 1 and curr_key3_state == 0:
        press_count += 1
        if press_count % 2 != 0:
            print("启动key3按钮代码")
        else:
            print("关闭key3按钮代码")
    prev_key3_state = curr_key3_state
    
