from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import requests
import json

app = Flask(__name__)

endpoint = 'Paste your model Url'
key = 'Paste your key'

# Set the content type in the request headers
request_headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + key}


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['Age'])
        gender = str(request.form['sexradio'])
        polyu = str(request.form['Polyuriaradio'])
        polyd = str(request.form['Polydipsiaradio'])
        Suwl = int(request.form['Sudden_weight_lossradio'])
        waek = int(request.form['Weaknessradio'])
        polyp = int(request.form['Polyphagiaradio'])
        genth = int(request.form['Genital_thrushradio'])
        viblu = int(request.form['Visual_blurringradio'])
        itching = int(request.form['Itchingradio'])
        irriti = int(request.form['Irritabilityradio'])
        dehea = int(request.form['Delayed_healing_radio'])
        parpa = int(request.form['Partial_paresisradio'])
        musstiff = int(request.form['Muscle_stiffnessradio'])
        alopecia = int(request.form['Alopeciaradio'])
        obesity = int(request.form['Obesityradio'])

        data = [[age, gender, polyu, polyd, Suwl, waek, polyp, genth, viblu,
                              itching, irriti, dehea, parpa, musstiff, alopecia, obesity]]
        input_json = json.dumps({"data": data})
        print("input: ",input_json)
        #Call the service
        response = requests.post(url=endpoint,data=input_json,headers=request_headers)

        # Get the predictions from the JSON response
        prediction = json.loads(response.json())
        print("pred : ",prediction[0])
        my_prediction = prediction[0]
        # Print the predicted class for each case.
        # for i in range(len(x_new)):
        #     print(x_new[i], predictions[i])
       
        return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
	app.run(debug=True)
