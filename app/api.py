from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route()
def hello():
    return "<p>Hello World.</p>"

@app.route('/json')
def get_json_data():
    file_path = 'all.json'  # Replace with your JSON file name
    data={}
    try:
        # Read the JSON file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        data = jsonify(data)
    except:
        print('error happened.')


    # Return the data as a JSON response
    return 

if __name__ == "__main__":
    app.run(port=5000)
