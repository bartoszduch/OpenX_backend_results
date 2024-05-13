from flask import Flask, request, jsonify
import uuid
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app_id = uuid.uuid4().hex


def convert_to_celsius(fare):
    return (fare - 32) * (5 / 9)


@app.route('/convert', methods=['GET'])
def convert_temp():

    fahrenheit_temp = request.args.get('fahrenheit', type=float)
    if fahrenheit_temp is None:
        return jsonify({"error": "No fahrenheit parameter provided"}), 400

    celsius_temp = round(convert_to_celsius(fahrenheit_temp),2)
    return jsonify({
        "celsius": celsius_temp,
        "app_id": app_id
    })


if __name__ == '__main__':
    app.run(debug=True)
