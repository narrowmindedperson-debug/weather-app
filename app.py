# ✅ What this Flask code does (in simple words)

# This file is your web controller.

# It:

# Shows the weather form (GET request)

# Accepts user input (POST request)

# Calls your weather engine (weather.py)

# Sends the weather data to index.html/*





import os
from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        city = request.form.get("cityName", "").strip()
        state = request.form.get("stateName", "").strip()
        country = request.form.get("countryName", "").strip()

        if not city:
            error = "Please enter a city."
        else:
            data = get_weather(city, state, country)
            if data is None:
                error = "City not found. Please check spelling."

    return render_template("index.html", data=data, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
