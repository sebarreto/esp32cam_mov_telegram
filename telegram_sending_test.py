import requests
# 1. This step allows us to identify our chat_id belonging our bot. We'll find it in the id field.
# TOKEN field is provided by botfather on Telegram.
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json()) # this return status and information.

# 2. This step is used to send a text message. After identiy chat_id field in step 1. You can comment this step if you want.
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# chat_id was printed in step 1.
chat_id = "yyyyyyyyyy"
message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message.

# 3. This step is for sending images.
# TOKEN field is provided by botfather on Telegram.
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# chat_id was printed in step 1.
chat_id = 'yyyyyyyyyy'
# URL Telegram API for photo sending.
url = f'https://api.telegram.org/bot{token}/sendPhoto'
# Image path on you local diskdrive. 
ruta_imagen = 'C:/xxxxx/yyyyy/zzzzzzz/test.jpg'
# Open file in binary mode.
with open(ruta_imagen, 'rb') as archivo:
    # Create a dictionary to hold the data.
    datos = {'chat_id': chat_id}
    archivos = {'photo': archivo}
    # Make POST request to Telegram with data attached.
    respuesta = requests.post(url, data=datos, files=archivos)
# Print the response.
print(respuesta.text)