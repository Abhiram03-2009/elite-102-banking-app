# Elite 102 Banking System

Welcome to the **Elite 102 Banking System App**! This application was built entirely in Python using SQLite designed specifically for the Code2College Elite 102 requirements. 

It handles robust account creation, deposit validations, secure withdrawals, and balance inquiries.

---

## ⚡ Features

### Terminal Application (`main.py`)
Provides a menu-driven, fully functional Command Line Interface to interact with the bank database perfectly hitting standard assignment criteria.

### SQLite Engine (`db.py`)
A pure Python backend layer powered by `sqlite3`! Automatically sets up schema relationships:
- `accounts` Table: ID, Name, Balance
- `transactions` Table: Timestamped history logs of every deposit and withdrawal.

### Flask Web Integration (`app.py`)
We went above and beyond the standard terminal requirements to include a **Flask Web Server**. The REST API runs on `localhost:5000` mapping JSON request/responses directly into Python SQLite logic.

---

## 🛠️ How To Run

**Requirements:**
- Python 3+
- `pip install flask flask-cors`

### Start the Terminal CLI 
```bash
python main.py
```
*Enjoy your sleek Python terminal user interface!*

### Start the Flask Server Backend
If you want to consume data over a web endpoint or custom React UI:
```bash
python app.py
```
*(Server will listen automatically on http://localhost:5000)*
