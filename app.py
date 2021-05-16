from flask import Flask, request, jsonify, abort
from flask.templating import render_template
from model import predict
from features import features_list

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    data = {}
    request_data = request.get_json()
    for feature in features_list:
        data.update({feature: request_data[feature]})
    prediction = predict(request.json)
    return jsonify({'done': True, 'prediction': prediction[0]}), 201


if __name__ == '__main__':
    app.run(debug=True)
