from flask import Flask, jsonify, request,render_template
import numpy as np
import pickle

app = Flask(__name__)


with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)
model_accuracy = 95.0 
@app.route('/')
def index():
    return render_template('index.html', model_accuracy=model_accuracy)

@app.route('/Submit', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('submit.html', prediction=None, model_accuracy=model_accuracy)
    
    elif request.method == 'POST':
        data = request.form.get("text")
        if not data:
            return render_template('submit.html', prediction="Please enter valid text.", model_accuracy=model_accuracy)
        
        try:
            prediction = model.predict([data])
            response = int(prediction[0]) if isinstance(prediction[0], np.integer) else prediction[0]
            return render_template('submit.html', prediction=response, model_accuracy=model_accuracy)
        except Exception as e:
            return render_template('submit.html', prediction=f"Error: {str(e)}", model_accuracy=model_accuracy)

if __name__ == '__main__':
    app.run(debug=True)

