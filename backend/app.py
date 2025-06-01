from flask import Flask, request, jsonify
from PIL import Image
import io, tensorflow as tf
from flask_cors import CORS

model = tf.keras.applications.MobileNetV2(weights='imagenet')
preprocess = tf.keras.applications.mobilenet_v2.preprocess_input
decode = tf.keras.applications.mobilenet_v2.decode_predictions

app = Flask(__name__)
CORS(app)
@app.route('/classify', methods=['POST'])
def classify():
    img_bytes = request.files['image'].read()
    img = Image.open(io.BytesIO(img_bytes)).resize((224,224))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = preprocess(tf.expand_dims(x,0))
    preds = model.predict(x)
    top3 = decode(preds, top=3)[0]
    return jsonify([{'label':l,'score':float(s)} for (_,l,s) in top3])

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
