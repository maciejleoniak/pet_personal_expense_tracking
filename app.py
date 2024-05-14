from flask import Flask, render_template, request, redirect, url_for
from expense import Expense

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_expense", methods=["POST"])
def add_expense():
    # Handle adding expense data from the form.
    expense_name = request.form.get("expense_name")
    expense_amount = float(request.form.get("expense_amount"))
    expense_category = request.form.get("expense_category")
    
    new_expense = Expense(name=expense_name, category=expense_category, amount=expense_amount)
    save_expense_to_file(new_expense, "expenses.csv")
    
    return redirect(url_for("index"))

def save_expense_to_file(expense: Expense, expense_file_path):
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

if __name__ == "__main__":
    app.run(debug=True)
