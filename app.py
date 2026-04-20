from flask import Flask, request, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app) # Allow cross-origin requests from our Vite React frontend

@app.route('/accounts', methods=['GET'])
def get_accounts():
    rows = db.list_accounts()
    accounts = [{'id': r[0], 'name': r[1], 'balance': r[2]} for r in rows]
    return jsonify(accounts)

@app.route('/accounts', methods=['POST'])
def create_acc():
    data = request.json
    name = data.get('name')
    initial_deposit = float(data.get('initial_deposit', 0))
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    try:
        acc_id = db.create_account(name, initial_deposit)
        return jsonify({'id': acc_id, 'name': name, 'balance': initial_deposit}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/accounts/<int:account_id>/deposit', methods=['POST'])
def handle_deposit(account_id):
    data = request.json
    amount = float(data.get('amount', 0))
    try:
        db.deposit(account_id, amount)
        balance = db.check_balance(account_id)
        return jsonify({'message': 'Deposit successful', 'balance': balance})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/accounts/<int:account_id>/withdraw', methods=['POST'])
def handle_withdraw(account_id):
    data = request.json
    amount = float(data.get('amount', 0))
    try:
        db.withdraw(account_id, amount)
        balance = db.check_balance(account_id)
        return jsonify({'message': 'Withdrawal successful', 'balance': balance})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    db.init_db() # Ensure DB is initialized before starting
    print("Starting CryptoVault Flask Server...")
    app.run(debug=True, port=5000)
