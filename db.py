import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'bank.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (account_id) REFERENCES accounts(id)
        )
    ''')
    conn.commit()
    conn.close()

def create_account(name, initial_deposit):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', (name, initial_deposit))
    account_id = cursor.lastrowid
    if initial_deposit > 0:
        cursor.execute('INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)', (account_id, 'DEPOSIT', initial_deposit))
    conn.commit()
    conn.close()
    return account_id

def deposit(account_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE accounts SET balance = balance + ? WHERE id = ?', (amount, account_id))
    if cursor.rowcount == 0:
        conn.close()
        raise ValueError("Account not found.")
    cursor.execute('INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)', (account_id, 'DEPOSIT', amount))
    conn.commit()
    conn.close()

def withdraw(account_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise ValueError("Account not found.")
    balance = row[0]
    if amount > balance:
        conn.close()
        raise ValueError("Insufficient funds.")
    cursor.execute('UPDATE accounts SET balance = balance - ? WHERE id = ?', (amount, account_id))
    cursor.execute('INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)', (account_id, 'WITHDRAWAL', amount))
    conn.commit()
    conn.close()

def check_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise ValueError("Account not found.")
    return row[0]

def list_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, balance FROM accounts')
    rows = cursor.fetchall()
    conn.close()
    return rows
