from flask import Flask
import pytesseract as pyt
from PIL import Image


app = Flask(__name__)
pyt.pytesseract.tesseract_cmd = r'C:\Users\SURIYAPRAKASH\AppData\Local\Tesseract-OCR\tesseract.exe'

im = Image.open('quote1.jpg')

#print(pyt.image_to_string(im))

@app.route("/")
def hello():
   return pyt.image_to_string(im)
#sd

if __name__ == '__main__':
    app.run(debug=True)
