import RPi.GPIO as GPIO
import time
from smbus import SMBus
import spidev
import ctypes

RST_PIN         = 25
DC_PIN          = 24
CS_PIN          = 8
BL_PIN          = 18

Device_SPI = 1
Device_I2C = 0

if(Device_SPI == 1):
    Device = Device_SPI
    spi = spidev.SpiDev(0, 0)
else :
    Device = Device_I2C
    address         = 0x3C
    bus = SMBus(1)

def digital_write(pin, value):
    GPIO.output(pin, value)

def digital_read(pin):
    return GPIO.input(BUSY_PIN)

def delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_writebyte(data):
    spi.writebytes([data[0]])

def i2c_writebyte(reg, value):
    bus.write_byte_data(address, reg, value)

def module_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RST_PIN, GPIO.OUT)
    GPIO.setup(DC_PIN, GPIO.OUT)
    GPIO.setup(CS_PIN, GPIO.OUT)
    GPIO.setup(BL_PIN, GPIO.OUT)
    
    if(Device == Device_SPI):
        spi.max_speed_hz = 10000000
        spi.mode = 0b00
    
    GPIO.output(CS_PIN, 0)
    GPIO.output(BL_PIN, 1)
    GPIO.output(DC_PIN, 0)
    return 0

def module_exit():
    if(Device == Device_SPI):
        spi.SYSFS_software_spi_end()
    else :
        bus.close()
    GPIO.output(RST_PIN, 0)
    GPIO.output(DC_PIN, 0)
    