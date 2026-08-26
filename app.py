from flask import Flask, render_template, request, redirect, session
import sqlite3

from college_data import colleges
from chatbot import get_bot_response

app = Flask(__name__)
app.secret_key = "college_ai_secret"


# ==========================================================
# DATABASE
# ==========================================================

def create_database():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT,
        mobile TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


create_database()


# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def home():
    return redirect("/login")


# ==========================================================
# REGISTER
# ==========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        if user:

            conn.close()

            return render_template(
                "register.html",
                message="⚠ Username already exists."
            )

        cursor.execute(
            """
            INSERT INTO users(username,email,mobile,password)
            VALUES(?,?,?,?)
            """,
            (username, email, mobile, password)
        )

        conn.commit()
        conn.close()

        return render_template(
            "login.html",
            message="✅ Registration Successful. Please Login."
        )

    return render_template("register.html")


# ==========================================================
# LOGIN
# ==========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        existing = cursor.fetchone()

        if not existing:

            conn.close()

            return render_template(
                "login.html",
                message="❌ Username not found."
            )

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user"] = username
            session["history"] = []
            session.pop("college", None)

            return redirect("/chatbot")

        return render_template(
            "login.html",
            message="❌ Incorrect Password."
        )

    return render_template("login.html")


# ==========================================================
# COLLEGE SELECTION
# ==========================================================

@app.route("/chatbot")
def chatbot():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "chatbot.html",
        colleges=colleges
    )


# ==========================================================
# CHAT PAGE
# ==========================================================

@app.route("/college/<college_name>", methods=["GET", "POST"])
def select_college(college_name):

    if "user" not in session:
        return redirect("/login")

    # If student opens another college
    if session.get("college") != college_name:

        session["college"] = college_name

        session["history"] = [

            {
                "user": "",
                "bot":
                f"👋 Welcome to {colleges[college_name]['name']}.\n\n"
                "I am your virtual college assistant.\n\n"
                "You can ask me about:\n"
                "• Courses\n"
                "• Fees\n"
                "• Admission\n"
                "• Eligibility\n"
                "• Cutoff\n"
                "• Placements\n"
                "• Hostel\n"
                "• Transport\n"
                "• Facilities\n"
                "• History\n"
                "• Vision\n"
                "• Mission\n"
                "• Exams\n"
                "• Contact\n"
                "• NAAC\n"
                "• NBA"
            }

        ]

    history = session["history"]

    if request.method == "POST":

        message = request.form["msg"]

        response = get_bot_response(
            college_name,
            message
        )

        history.append({

            "user": message,

            "bot": response

        })

        session["history"] = history

    return render_template(

        "chat.html",

        college=colleges[college_name],

        history=history

    )


# ==========================================================
# LOGOUT
# ==========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)     