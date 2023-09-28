
from flask import Flask, request, jsonify, render_template
import sqlite3

# Initialize the Flask application
app = Flask(__name__, static_folder='static', static_url_path='/static')

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('expense_tracker.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, description TEXT, amount REAL, date TEXT)")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

# Create a new expense
@app.route('/expense', methods=['POST'])
def add_expense():
    try:
        data = request.json
        category = data['category']
        description = data['description']
        amount = data['amount']
        date = data['date']
        
        conn = sqlite3.connect('expense_tracker.db')
        c = conn.cursor()
        c.execute("INSERT INTO expenses (category, description, amount, date) VALUES (?, ?, ?, ?)", (category, description, amount, date))
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success", "message": "Expense added successfully!"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Get all expenses
@app.route('/expenses', methods=['GET'])
def get_expenses():
    try:
        conn = sqlite3.connect('expense_tracker.db')
        c = conn.cursor()
        c.execute("SELECT * FROM expenses")
        rows = c.fetchall()
        conn.close()
        
        expenses = [{"id": row[0], "category": row[1], "description": row[2], "amount": row[3], "date": row[4]} for row in rows]
        return jsonify({"status": "success", "expenses": expenses}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# To run the app
if __name__ == '__main__':
    app.run(debug=True)
