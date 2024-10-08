from flask import Flask, request, jsonify
import tensorflow as tf
from flask_cors import CORS
import numpy as np
import imageio.v2 as imageio

app = Flask(__name__)
CORS(app)

MODEL = tf.keras.models.load_model('../potatoes.h5')
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data):
    image = imageio.imread(data)
    return image

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return 'No file part'

        file = request.files['image']
        image = read_file_as_image(file.read())
        img_batch = np.expand_dims(image, 0)

        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        return predicted_class
    except Exception as e:
        return "ITS AN EROR"
if __name__ == '__main__':
    app.run(debug=True)