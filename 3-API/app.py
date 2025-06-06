from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "data.db"

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = cursor.execute(query).fetchone()
    conn.close()

    if result:
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

@app.route("/debug", methods=["GET"])
def debug():
    return jsonify({
        "env": dict(os.environ),
        "path": os.getcwd()
    })

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    f.save(f"./uploads/{f.filename}")
    return jsonify({"status": "uploaded"})
