from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/semester")
def semester():
    return render_template("semester.html")


@app.route("/formulas")
def formulas():
    return render_template("formulas.html")


@app.route("/cpr")
def cpr():
    return render_template("cpr.html")


@app.route("/cpr/calculator")
def cpr_calculator():
    return render_template("cpr_calculator.html")


@app.route("/cpr/concept")
def cpr_concept():
    return render_template("concept.html")


if __name__ == "__main__":
    app.run(debug=True)