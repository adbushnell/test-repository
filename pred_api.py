from flask import Flask, jsonify, request
import os
import pickle
import numpy as np

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, 'saved_model')

@app.route('/')
def home():
    return jsonify(data='Input height and weight to discover if you are healthy!')


model = pickle.load(open(model_path, 'rb'))

@app.route('/get_healthy_pred')
def get_healthy_pred():

    height = float(request.args.get('height', 'unknown'))
    weight = float(request.args.get('weight', 'unknown'))

    if (weight != 'unknown') & (height != 'unknown'):

        pred = model.predict(np.array((height, weight)).reshape(1, -1))[0]

    else:

        pred = 'Not enough info'

    return jsonify(is_healthy=float(pred))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

