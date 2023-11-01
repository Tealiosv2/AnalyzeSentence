from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    input_text = request.form.get("input_text")

    # Process the input_text here and obtain label and score
    # For this example, let's assume label and score are calculated.
    label = "Positive"  # Replace with the actual label
    score = 0.85  # Replace with the actual score

    return render_template("result.html", label=label, score=score)


if __name__ == "__main__":
    app.run(debug=True)