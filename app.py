import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)
model = load('customer_clftree.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    #int_features = [int(x) for x in request.form.values()]
    int_features = []
    for x in request.form.values():
        print(x,x.isdigit())
        if x.isdigit() :
            int_features.append(int(x))
        else:
            int_features.append(float(x))
    
    
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = prediction[0]#round(prediction[0],2)
    
    return render_template('index.html', prediction_text=output)

@app.route('/results',methods=['POST'])
def results():
    
    data = request.get_json(force=True)
    
    prediction = model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)