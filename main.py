from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    prediction_type = ""

    if request.method == "POST":

        message = request.form.get("message")

        if not message or message.strip() == "":
            result = "⚠ Please enter a message."
            prediction_type = "warning"

        else:

            data = vectorizer.transform([message])

            prediction = model.predict(data)

            if prediction[0] == 1:
                result = "🚨 Spam Message"
                prediction_type = "spam"

            else:
                result = "✅ Not Spam Message"
                prediction_type = "safe"

    return render_template(
        "index.html",
        result=result,
        prediction_type=prediction_type
    )


# ==========================
# ABOUT PAGE
# ==========================

@app.route("/about")
def about():
    return render_template("about.html")


# ==========================
# FEATURES PAGE
# ==========================

@app.route("/features")
def features():
    return render_template("features.html")


# ==========================
# CONTACT PAGE
# ==========================

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)