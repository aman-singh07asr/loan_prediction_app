from flask import Flask, render_template, request
app = Flask(__name__)

# Dummy prediction logic
def predict_loan_approval(data):
    if data['income'] > 30000 and data['credit_score'] > 650:
        return "Approved"
    return "Rejected"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'name': request.form['name'],
        'occupation': request.form['occupation'],
        'income': int(request.form['income']),
        'age': int(request.form['age']),
        'loan_amount': int(request.form['loan_amount']),
        'loan_term': int(request.form['loan_term']),
        'credit_score': int(request.form['credit_score']),
        'employment_type': request.form['employment_type']
    }

    prediction = predict_loan_approval(data)
    return render_template('result.html', name=data['name'], result=prediction)

if __name__ == '__main__':
    app.run(debug=True)
