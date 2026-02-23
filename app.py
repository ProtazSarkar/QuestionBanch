from flask import Flask, render_template, request, redirect, send_file,jsonify
import os

from config.config import CONFIG_DIR, ROOT_DIR

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():
    print("server is running")
    return render_template("index.html")


# ---------------- GENERATE PDF ----------------
@app.route("/generate", methods=["POST"])
def generate():
    data = request.json   # no ()
    questions = data.get("questions")

    print(questions)

    return jsonify({
    "message":"Question recieved "
    })


# ---------------- DOWNLOAD ----------------
@app.route("/download", methods=["GET"])
def download():
    file_path = os.path.join(ROOT_DIR, "output.pdf")

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )