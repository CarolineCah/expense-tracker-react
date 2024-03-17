from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add-expense', methods=['POST'])
def add_expense():
    expense_data = request.form
    expenses.append({
        'id': len(expenses) + 1,
        'name': expense_data['name'],
        'amount': expense_data['amount'],
        'category': expense_data['category']
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
