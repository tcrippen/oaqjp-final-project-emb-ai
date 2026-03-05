from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def detect_emotion(text):
    """
    Temporary placeholder emotion detector
    until Watson API is integrated.
    """
    if "happy" in text.lower():
        return "joy"
    if "sad" in text.lower():
        return "sadness"
    if "angry" in text.lower():
        return "anger"

    return "neutral"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotion", methods=["POST"])
def emotion():
    data = request.json
    text = data.get("text", "")

    emotion = detect_emotion(text)

    return jsonify({
        "text": text,
        "emotion": emotion
    })


if __name__ == "__main__":
    app.run(debug=True)