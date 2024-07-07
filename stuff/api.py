python
from flask import Flask,request, jsonify

app=Flask(__name__)

import pandas as pd
food_data =pd.read_excel("https://docs.google.com/spreadsheets/d/1oEdqdbqths-yDj9bpuVe9btKLWMVznY_oa5hCebtaYI/edit?usp=sharing")

print(food_data.head())
print()
print(food_data.tail())

if __name__=="__main__":
    app.run()
   @app.route('/people' ,methods=['GET'])
    def get_people()
        return jsonify(get_people)



@app.route('/people/new',methods=['post'])
def create_person():
    new_person={
       "id":len(people)+1,
       "name":request.json['name'],
        "age":request.json['age'],
        "job":request.json['job'],
    }


    
    people.append(new_person)
    return jsonify(new_person), 201








from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/json')
def get_json_data():
    file_path = 'all.json'  # Replace with your JSON file name

    # Read the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Return the data as a JSON response
    return jsonify(data)

if name == "__main__":
    app.run(port=5000)

