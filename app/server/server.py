from flask import Flask, render_template
import logging

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
