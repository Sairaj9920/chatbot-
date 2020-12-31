from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import json
import requests
import extract 
import sys  
import os
import numpy as np
import joblib
import systemcheck

app = Flask(__name__)
app.secret_key = 'encryption_key'

@app.route('/', methods=['get', 'post'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        session['name'] = name
        if name not in os.listdir():
            os.mkdir(f"{name}")
        try:
            print(list(request.files))
            for file in request.files.getlist('allFiles'):
                file.save(os.path.join(name,file.filename))    
        except(Exception) as e:
            print(e)
        extract.extract(session['name'])
        return redirect(url_for('ai'))
    return render_template('inputForm.html')


@app.route('/ai/')
def ai():
    return render_template('chatScreen.html', name=session['name'])



                
@app.route('/machineLearning/<msg>', methods=['get', 'post'])
def machine_learning(msg):
    print(msg)
    data1 = json.dumps({"sender": "Rasa","message": msg})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res1 = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data1, headers = headers)
    res1 = res1.json()
    print(res1)
    try:
        if len(res1)>=2:
            s=res1[0]['text']+"\n\n\n"+res1[1]['text']
            res1=s
        if len(res1)<2:
            res1=res1[0]['text']
    except:
        res1="please can you repeat the last response"
    return jsonify(data=res1)


if __name__ == '__main__':
    app.run(port=8008,debug=True,threaded=True)

