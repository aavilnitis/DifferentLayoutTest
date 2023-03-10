from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from packages.extensions import db
from packages.models import MenuItem
from customer.customer import customer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

app.register_blueprint(customer, url_prefix="/")


@app.route("/")
def home():
    return render_template("base.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
