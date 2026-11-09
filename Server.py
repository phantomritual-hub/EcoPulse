from flask import Flask,render_template
import os
app = Flask(__name__)
@app.route("/")
def show():
    return render_template("EcoPulse.html")

@app.route("/birthday_Test")
def run():
    return render_template("Index.html")


@app.route("/Wakeup_Call",methods=['POST'])
def returnCall():
    webURL = request.json
    time.sleep(14*60+50)
    requests.post("https://school-project-name.onrender.com/Wakeup_Call",data = "https://ecopulse-73io.onrender.com")
    return "wake up call sent"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=10000)