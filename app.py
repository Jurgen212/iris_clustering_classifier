from flask import Flask, render_template, request

import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo
with open('AdaBoostClassifier.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    response = None
    if request.method == 'POST':    
        try:
            sepal_length = float(request.form['sepalLengthCm'])
            sepal_width = float(request.form['sepalWidthCm'])
            petal_length = float(request.form['petalLengthCm'])
            petal_width = float(request.form['petalWidthCm'])

            features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            reverse_mapping = {1: 'Iris-setosa', 0: 'Iris-versicolor', 2: 'Iris-virginica'}

            prediction = model.predict(features)[0]
            response = reverse_mapping.get(prediction, 'Desconocido')
        except Exception as e:
            response = f'Error: {str(e)}'

    return render_template('index.html', prediction=response)

if __name__ == '__main__':
    app.run(debug=True)