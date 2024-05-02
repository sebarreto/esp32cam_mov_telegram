# esp32cam_mov_telegram
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

![Arduino wires]([https://lastminuteengineers.com/wp-content/uploads/featuredimages/Project-Interfacing-Passive-Infrared-PIR-Sensor-with-Arduino-Uno.webp](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/A_few_Jumper_Wires.jpg/800px-A_few_Jumper_Wires.jpg))

**Protoboard**
It's not mandatory. It's recommended.

![Protoboard](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Protoboard_Unitec.jpg/800px-Protoboard_Unitec.jpg?20141110214556)

## General schematic

![schematic ESP32CAM + PIR](https://hackster.imgix.net/uploads/attachments/1505171/sketch_7UFbaJbbxS.png?auto=compress%2Cformat&w=740&h=555&fit=max)
