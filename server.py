# For file management.
import os
# To handle images in base64 format.
import base64
# To add date time in new images name.
from datetime import datetime
# For server management.
from flask import Flask, request

app = Flask(__name__)
# This is the main method of the app, called from ESP32.
@app.route('/save_photo', methods=['POST'])
def save_photo():
# If we received data from ESP32 then we'll decode base64 image.
    if 'image_base64' in request.json:
        image_base64 = request.json['image_base64']
        try:
            # Base64 decode.
            image_decode = base64.b64decode(image_base64)
            # Catch date time from system.
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Create new image name
            file_name = f"imagen_{current_time}.jpg"
            # Saving new image on local repository.
            with open(os.path.join('C:/xxxxx/yyyy/zzzzz/', file_name), 'wb') as f:
                f.write(image_decode)
            telegram_sending(file_name)
            return 'Photo received and saved it.'
        except Exception as e:
            return f'Error procesing image: {str(e)}', 500
    else:
        return 'Base64 image did not received.', 400

def telegram_sending(file_name):
    import requests
    # TOKEN field is provided by botfather on Telegram.
    token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # Our bot chat_id.
    chat_id = 'yyyyyy'
    # URL Telegram API for photo sending.
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    # Image path on you local diskdrive.
    image_path = 'C:/xxxxx/yyyy/zzzzz/' + file_name
    # Open file in binary mode.
    with open(image_path, 'rb') as t_file:
        # Create a dictionary to hold the data.
        t_data = {'chat_id': chat_id}
        t_files = {'photo': t_file}
        # Make POST request to Telegram with data attached.
        t_response = requests.post(url, data=t_data, files=t_files)
    # Print the response.
    print(t_response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
