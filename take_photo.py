from machine import Pin
import time
# Thanks to https://github.com/lemariva/micropython-camera-driver you can find more information there.
import camera
import gc
import urequests
# To Wi-Fi connection
import network
import ubinascii
# PIR sensor PIN. It's locatted in PIN 21.
pir = Pin(21, Pin.IN, Pin.PULL_DOWN)

# Wi-Fi connection method.
def wifi_connection(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('Connecting to wifi...')
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Wi-Fi connection established:', wlan.ifconfig())

# Take photo with ESP32-CAM
def take_photo(nombre= 'Photo.jpeg', voltear= 0, espejo= 1):    
    camera.init()    
    buf = camera.capture()
    f = open(nombre, "wb")
    f.write(buf)
    f.close()
    camera.deinit()
    return buf

# Conexión y envío de foto
def connection_send():    
    led_flash = Pin(4, Pin.OUT)
    led_flash.on()
    gc.collect()
    buf = take_photo()
    # Your ssid & password - Wi-Fi network
    wifi_connection('XXXXXXXXXX', 'YYYYYYYYYYYYYY')
    # Sending photo by HTTP POST request
    photo_base64 = ubinascii.b2a_base64(buf)
    url = 'http://xxx.xxx.xxx.xxx:5000/save_photo'  # You need to use the url provided by Flask Server.
    files = {'photo': 'photo', 'image_base64': photo_base64}  # photo name and base64 data.
    # Sending photo by POST
    try:
        response = urequests.post(url, json=files)
        if response.status_code == 200:
            print('Photo successfully saved.')
        else:
            print('Error saving photo:', response.status_code)
    except Exception as e:
        print('Error sending photo:', e)
    led_flash.off()
# Main loop - movement sensor.
while True:
    if pir.value() ==1: 
        print("Movement detected") 
        connection_send()
        time.sleep(2)
    else:
        print("No movement")
        time.sleep(1)
# you can change frequency and sleeping time.