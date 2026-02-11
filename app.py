# ✅ What this Flask code does (in simple words)

# This file is your web controller.

# It:

# Shows the weather form (GET request)

# Accepts user input (POST request)

# Calls your weather engine (weather.py)

# Sends the weather data to index.html/*





from flask import Flask, render_template, request

from weather import main as get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.method == "POST":
        city = request.form .get("cityName")
        state = request.form .get("stateName")
        country= request.form .get("countryName")
        data=(get_weather(city, state, country))
    return render_template("index.html", data=data  )

if __name__ == "__main__":
    app.run(debug=True)