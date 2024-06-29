from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__ )

# Load the model
model = load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.form.to_dict()
    input_data = [int(value) for value in data.values()]
    input_data.insert(0 , 10)
    input_data.insert(1 , 0)
    print(len(input_data))
    prediction = model.predict([input_data])

    # return jsonify({'prediction': int(prediction[0])})
    return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    app.run()
