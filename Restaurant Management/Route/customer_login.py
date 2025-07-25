from flask import Blueprint, render_template, request
from models import cursor, db

# Creating a Blueprint
login_bp = Blueprint("login", __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def customer_login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            login="username and password are required"
        else:
            return render_template("customer.html")
        cursor.execute("INSERT INTO customer_login (username, password) VALUES (%s, %s)", (username,password))
        db.commit()

    # cursor.execute("SELECT * FROM customer_login")
    login = cursor.fetchall()
    return render_template("customer_login.html",login=login)

