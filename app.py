from flask import Flask
import views

app = Flask(__name__)

# Register routes
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/add_expense', 'add_expense', views.add_expense, methods=['POST'])
app.add_url_rule('/set_up_budget', 'set_up_budget', views.set_up_budget, methods=['POST'])
app.add_url_rule('/show_budget', 'show_budget', views.show_budget, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True)
