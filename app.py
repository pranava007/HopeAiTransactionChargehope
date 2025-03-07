from flask import Flask, render_template, request
from function import calculate_fee_and_check_equality

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inpute.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        try:
            fee_amount = float(request.form['feeAmount'])
            transaction_charge = float(request.form['transaction'])

            request_Amount, trans_Amount, original_fee_Amount, transactions = calculate_fee_and_check_equality(
                fee_amount, transaction_charge
            )

            context = {
                'request_Amount': request_Amount,
                'trans_Amount': trans_Amount,
                'original_fee_Amount': original_fee_Amount,
                'transactions': transactions,
            }

            return render_template('outpute.html', **context)
        except ValueError:
            return "Invalid input. Please enter numerical values."

if __name__ == '__main__':
    app.run(debug=True)
