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

    generated_text = text_generation_pipeline(input_text, max_length=30, do_sample=True, top_k=50, top_p=0.95)[0][
        'generated_text']

    similar_phrase = generated_text.strip()

    return render_template("index.html", label=label, score=score, alternative_statement=similar_phrase)


if __name__ == "__main__":

    app.run()
