from flask import Flask, render_template, request
from transformers import pipeline
import os

app = Flask(__name__)

sentiment_pipeline = pipeline("sentiment-analysis")
text_generation_pipeline = pipeline("text-generation")


@app.route("/", methods=["GET"])
def index():

    return render_template("index.html", label="", score="")


@app.route("/process", methods=["POST"])
def process():
    input_text = request.form.get("input_text")

    sentiment_analysis = pipeline('sentiment-analysis')
    sentiment_analysis(input_text)

    label = sentiment_analysis(input_text)[0]['label']
    score = sentiment_analysis(input_text)[0]['score']

    generated_text = text_generation_pipeline(input_text, max_length=50, num_return_sequences=1)[0]['generated_text']

    rephrased_suggestion = generated_text.strip()

    return render_template("index.html", label=label, score=score, alternative_statement=rephrased_suggestion)


if __name__ == "__main__":

    app.run()
