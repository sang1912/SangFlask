from flask import Flask, render_template, send_file
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    # Tạo ảnh
    img = Image.new('RGB', (200, 200), color='red')
    img.save('example.jpg')  # Lưu ảnh với tên là example.jpg

    return render_template('index.html', image_path='example.jpg')

@app.route('/image/<path:filename>')
def get_image(filename):
    # Trả về ảnh từ đường dẫn
    return send_file(filename, mimetype='image/jpeg')

@app.route('/fetch_image')

def fetch_image():
    # URL của ảnh cần tải
    image_url = 'https://firebasestorage.googleapis.com/v0/b/looka-e5275.appspot.com/o/clothes%2Fdownload%20(1).jpeg?alt=media&token=49373e40-50ef-4174-943e-0fb98a7122b2'

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save('logo.jpg')  # Lưu ảnh với tên là logo.jpg

    return render_template('index.html', image_path='logo.jpg')
if __name__ == '__main__':
    app.run(debug=True)