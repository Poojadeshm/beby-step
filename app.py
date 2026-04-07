from flask import Flask, jsonify, request, render_template
from data import food_data, sleep_data, prayers

app = Flask(__name__)

# 🟢 Home Route
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

# 🟢 Get Food Routine
@app.route("/food", methods=["GET"])
def get_food():
    return jsonify(food_data)

# 🟢 Get Sleep Time
@app.route("/sleep", methods=["GET"])
def get_sleep():
    return jsonify(sleep_data)

# 🟢 Update Sleep Time
@app.route("/sleep", methods=["POST"])
def update_sleep():
    data = request.json
    sleep_data["bedtime"] = data.get("bedtime", sleep_data["bedtime"])
    sleep_data["nap_time"] = data.get("nap_time", sleep_data["nap_time"])
    return jsonify({"message": "Sleep updated!", "sleep": sleep_data})

# 🟢 Get Prayers
@app.route("/prayers", methods=["GET"])
def get_prayers():
    return jsonify(prayers)

# 🟢 Add New Meal (Optional Feature)
@app.route("/add_meal", methods=["POST"])
def add_meal():
    data = request.json
    time = data.get("time")
    meal = data.get("meal")
    recipe = data.get("recipe")

    if time and meal:
        food_data[time] = {"meal": meal, "recipe": recipe}
        return jsonify({"message": "Meal added!", "food": food_data})
    else:
        return jsonify({"error": "Invalid data"}), 400

# ▶ Run App
if __name__ == "__main__":
    app.run(debug=True)