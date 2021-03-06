
from flask import Flask,jsonify, request
import numpy as np
import joblib
import pandas as pd
import numpy as np

import pickle


import flask
app= Flask(__name__,template_folder='template')
model = joblib.load('model1.pkl')

@app.route('/',methods=['GET'])

def home():
    return flask.render_template('ind.html')
    
    
@app.route("/predict", methods=["POST"])
def predict():
    
    if request.method == 'POST':
        
        age=int(request.form['age'])
        
        height=int(request.form['height'])
        Weight=float(request.form['Weight'])
        Diabetic_patient=request.form['Diabetic_patient']
        if(Diabetic_patient=='Yes'):
            Diabetic_patient=1
                
        else:
            Diabetic_patient=0
           
        
        BP_problem=request.form['BP_problem']
        if(BP_problem=='Yes'):
            BP_problem=1
        else:
            BP_problem=0	
            
        transplants=request.form['transplants']
        if(transplants=='Yes'):
            transplants=1
        else:
            transplants=0
            
        chron=request.form['chron']
        if(chron=='Yes'):
            chron=1
        else:
            chron=0
            
        allergy=request.form['allergy']
        if(allergy=='Yes'):
            allergy=1
        else:
            allergy=0
            
        cancer=request.form['cancer']
        if(cancer=='Yes'):
            cancer=1
        else:
            cancer=0
           
        surg=int(request.form['surg'])
        
    
            
        prediction=model.predict([[age,height,Weight,Diabetic_patient,BP_problem,transplants,chron,allergy,cancer,surg]])
        output=round(prediction[0],2)
        
        return flask.render_template('result.html', prediction_text='The Predicted Premiumprice is {}'.format(output))
    else:
        return flask.render_template('ind.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8081,debug=True)
