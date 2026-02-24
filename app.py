from flask import Flask, render_template, request, redirect, send_file,jsonify
import os

from config.config import CONFIG_DIR, ROOT_DIR

from services.createPaper import CREATE_PAPER

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():
    print("server is running")
    return render_template("index.html")


# ---------------- GENERATE PDF ----------------
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()   # safer than request.json
    questions = data.get("questions", [])

    if not questions:
        return jsonify({"status": "error", "message": "No questions provided"}), 400

    paper = CREATE_PAPER()
    paper.install_formates("questions")

    try:
        for idx, content in enumerate(questions, start=1):
            paper.add_question(idx, content, 10)

        paper.generate_pdf("output")

        return jsonify({"status": "success"})

    except Exception as e:
        print("PDF generation error:", e)
        return jsonify({"status": "error", "message": "PDF generation failed"}), 500

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