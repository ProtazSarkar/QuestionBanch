from flask import Flask,render_template

from config.config import CONFIG_DIR,ROOT_DIR

app=Flask(__name__)

@app.route("/")
def home():
    print("server is running")
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(
    
    host="0.0.0.0",
    port=5000,
    debug=True
    
    )