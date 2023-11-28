import SH1106
import time
import config
import traceback
import subprocess
import shutil
import psutil
import speedtest
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont


def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    disk_space = round(used / (2**30),2)
    disk_percent = round((used / total) * 100)
    return disk_space, disk_percent
 
def get_memory_usage():
    mem = psutil.virtual_memory()
    memory_usage = round(mem.used / (2**30),3)
    memory_percent = round((mem.used / mem.total) * 100)
    return memory_usage, memory_percent
 
def get_cpu_temperature():
    temperature = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"]).decode("utf-8")
    cpu_temp = float(temperature) / 1000
    return cpu_temp
 
def get_ip_address():
    ip_address = subprocess.check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
    return ip_address
    
def get_network_speed():
    old_value_sent = psutil.net_io_counters().bytes_sent
    old_value_recv = psutil.net_io_counters().bytes_recv
    time.sleep(1)
    new_value_sent = psutil.net_io_counters().bytes_sent
    new_value_recv = psutil.net_io_counters().bytes_recv
    speed_sent = round((new_value_sent - old_value_sent)/1024,1)
    speed_recv = round((new_value_recv - old_value_recv)/1024,1)
    return speed_recv,speed_sent
        

try:
    disp = SH1106.SH1106()
    disp.Init()
    disp.clear()

    font11 = ImageFont.truetype('Font.ttf',11)
 
    ip_address = get_ip_address()
 
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw1 = ImageDraw.Draw(image1)
    cpu_temperature = get_cpu_temperature()
    disk_space, disk_percent = get_disk_usage()
    memory_usage, memory_percent = get_memory_usage()
    upload_speed,download_speed = get_network_speed()
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    time_time = now.strftime("%H:%M:%S")

    draw1.text((50,14), "{} GB/{}%".format(memory_usage, memory_percent), font = font11, fill = 0)
    draw1.text((50,26), "{} GB/{}%".format(disk_space,disk_percent), font = font11, fill = 0)
    draw1.text((10,38), "{}kb/s".format(download_speed), font = font11, fill = 0)
    draw1.text((70,38), "{}kb/s".format(upload_speed), font = font11, fill = 0)
    draw1.text((10,50), "{}°C".format(cpu_temperature), font = font11, fill = 0)
    draw1.text((70,50), "{}".format(time_time), font = font11, fill = 0)
    draw1.line([(0,0),(127,0)], fill = 0)
    draw1.line([(0,0),(0,19)], fill = 0)
    draw1.line([(0,44),(0,63)], fill = 0)
    draw1.line([(0,63),(127,63)], fill = 0)
    draw1.line([(127,0),(127,19)], fill = 0)
    draw1.line([(127,44),(127,63)], fill = 0)
    draw1.line([(63,44),(63,63)], fill = 0)
    draw1.text((10,2), "IP  {}".format(ip_address), font = font11, fill = 0)
    draw1.text((10,14), "RAM => ", font = font11, fill = 0)
    draw1.text((10,26), "DISK=> ", font = font11, fill = 0)
    disp.ShowImage(disp.getbuffer(image1))
    
    while True: 
      
      image2 = Image.new('1', (disp.width, disp.height), "WHITE")
      draw2 = ImageDraw.Draw(image2)
      
      cpu_temperature = get_cpu_temperature()
      disk_space, disk_percent = get_disk_usage()
      memory_usage, memory_percent = get_memory_usage()
      download_speed,upload_speed = get_network_speed()
      now = datetime.now()
      current_time = now.strftime("%Y-%m-%d")
      time_time = now.strftime("%H:%M:%S")

      draw2.text((50,14), "{} GB/{}%".format(memory_usage, memory_percent), font = font11, fill = 0)
      draw2.text((50,26), "{} GB/{}%".format(disk_space,disk_percent), font = font11, fill = 0)
      draw2.text((10,38), "{}kb/s".format(download_speed), font = font11, fill = 0)
      draw2.text((70,38), "{}kb/s".format(upload_speed), font = font11, fill = 0)
      draw2.text((10,50), "{}°C".format(cpu_temperature), font = font11, fill = 0)
      draw2.text((70,50), "{}".format(time_time), font = font11, fill = 0)
      draw2.line([(0,0),(127,0)], fill = 0)
      draw2.line([(0,0),(0,19)], fill = 0)
      draw2.line([(0,44),(0,63)], fill = 0)
      draw2.line([(0,63),(127,63)], fill = 0)
      draw2.line([(127,0),(127,19)], fill = 0)
      draw2.line([(127,44),(127,63)], fill = 0)
      draw2.line([(63,44),(63,63)], fill = 0)
      draw2.text((10,2), "IP  {}".format(ip_address), font = font11, fill = 0)
      draw2.text((10,14), "RAM => ", font = font11, fill = 0)
      draw2.text((10,26), "DISK=> ", font = font11, fill = 0)
    
      disp.ShowImage(disp.getbuffer(image2))
      image1, image2 = image2, image1


except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    exit()
