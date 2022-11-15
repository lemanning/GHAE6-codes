import time
import network
import socket
from machine import Pin
led = Pin(15,Pin.out)
ledState="led State Unknown"

butto =Pin(16,Pin.IN,Pin.PULL_UP)

ssid=''
pasword=''
wlan=network.WLAN(network.STA_IF)
wln.active(True)
wlan.connect(ssid,password)

import time
import network

