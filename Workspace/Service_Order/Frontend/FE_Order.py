from flask import Flask, render_template

app = Flask(__name__)

@app.route("/orders")
def products():
    return render_template("orders.html")

if __name__ == "__main__":
    app.run(port=9002, debug=True)
