from flask import Blueprint, render_template
from packages.extensions import db
from packages.models import MenuItem

customer = Blueprint("customer", __name__, template_folder="templates")


@customer.route("/menu")
def menu():
    menu_items = MenuItem.query.all()
    return render_template("menu.html", menu_items=menu_items)
