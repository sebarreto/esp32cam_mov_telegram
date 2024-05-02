# MicroPython - esp32cam_mov_telegram
Movement detection using PIR sensor + ESP32CAM and sending images by Telegram.

## Hardware requirements

**ESP32-CAM**

I used ESP32-S2-WROOM board. Model FNK0085. Brand Freenove.

![ESP32-CAM](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2023/01/Freenove-ESP32.png?w=300&quality=100&strip=all&ssl=1)

Documentation: http://freenove.com/fnk0085
official store: https://store.freenove.com/

**PIR Sensor HC-SR501**

PIR sensor allows us to detect movements. It's cheap, it's not the best quality, but it's enough for this project.

![PIR Sensor HC-SR501](https://lastminuteengineers.com/wp-content/uploads/featuredimages/Project-Interfacing-Passive-Infrared-PIR-Sensor-with-Arduino-Uno.webp)

How it works: https://lastminuteengineers.com/pir-sensor-arduino-tutorial/ 

**Wires**

Wires male female connector. It'll depend if you used protoboard or not.

![Arduino wires](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/A_few_Jumper_Wires.jpg/800px-A_few_Jumper_Wires.jpg)

**Protoboard**

It's not mandatory. It's recommended.

![Protoboard](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Protoboard_Unitec.jpg/800px-Protoboard_Unitec.jpg?20141110214556)


## General schematic

![schematic ESP32CAM + PIR](https://hackster.imgix.net/uploads/attachments/1505171/sketch_7UFbaJbbxS.png?auto=compress%2Cformat&w=740&h=555&fit=max)

## MicroPython

1. Install Thonny IDE. You can also use Visual Studio or other. I recommend Thonny because is easy to use.
   (https://thonny.org/)
   
   You can find here installation step by step and first configuration (https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/)

2. ESP32-CAM firmware.

   I've tested a lot of firmware for my ESP32-CAM model. Best results obtained with (https://github.com/shariltumin/esp32-cam-micropython-2022/tree/main/X23/esp32s3-freenove/firmwares)

   Download firmware from shariltumin folder and flash ESP32-CAM from Thonny IDE.
   
3. MicroPython scripts.

   Download cam_config.py and take_photo.py. Save both scripts into ESP32-CAM with Thonny IDE.
   ![Thonny files](https://images2.imgbox.com/21/dd/ftol3MFN_o.png)

4. Change Wi-Fi credential (ssid, password). Use your own credentials.
   
## Server

1. Download server.py. Open it with Visual Studio IDE.
   Install Python. Instruccions here: (https://www.python.org/downloads/)
   Install required libraries. Instructions here: (https://packaging.python.org/en/latest/tutorials/installing-packages/)
   
2. Execute server.py. I used port 5000. You can use another port.
   ![Python flask server](https://images2.imgbox.com/cc/d3/QLDXBqCn_o.png)
   
3. Edit URL field(take_photo.py) with Thonny. Put IP address provided by Flask Server.

## Telegram

1. Create a bot with botfhater. Check here: (https://core.telegram.org/bots/tutorial) or here: (https://www.directual.com/lesson-library/how-to-create-a-telegram-bot)
   Save your TOKEN.
   
2. Download script telegram_sending_test.py use it to identify your bot CHAT-ID. (just step 1 is required).
   
3. Edit server.py to put your CHAT-ID.

## Execute from Thonny.

1. Save scripts into ESP32-CAM (cam_config.py and take_photo.py).
   
2. Keep Flask server running.

A lot of improvements could be done. For instance, you can practice and try to send pictures directly from ESP32-CAM to telegram.

**Check:** (https://micropython.org/)

**Special thanks:**
- https://www.youtube.com/watch?v=ukWvHX-JTgI&list=WL&index=36
- https://atareao.es/tutorial/crea-tu-propio-bot-para-telegram/bot-en-python-para-telegram/
- https://github.com/ComputadorasySensores/Capitulo79
- https://github.com/shariltumin/esp32-cam-micropython-2022/tree/main
- https://github.com/hapena/esp32cam
- https://micropython.org/

