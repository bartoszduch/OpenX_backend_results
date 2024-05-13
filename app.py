from flask import Flask, request, jsonify
import uuid
from flask_cors import CORS

# Create a new Flask application
app = Flask(__name__)
CORS(app)
app_id = uuid.uuid4().hex #Generate unique id

def convert_to_celsius(fare):
    return (fare - 32) * (5 / 9) #Function that convert farenheits to celcius


@app.route('/convert', methods=['GET'])
def convert_temp():
    #Get fahrenheit parametr from URL
    fahrenheit_temp = request.args.get('fahrenheit', type=float)
    if fahrenheit_temp is None:
        return jsonify({"error": "No fahrenheit parameter provided"}), 400
    #Convert to Celsius and round it
    celsius_temp = round(convert_to_celsius(fahrenheit_temp),2)
    #Return JSON format
    return jsonify({
        "celsius": celsius_temp,
        "app_id": app_id
    })

#Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
