from machinetranslation.translator import french_to_english, english_to_french
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    res = english_to_french(textToTranslate)
    return "Translated text to French:" + " " + str(res)

@app.route("/frenchToEnglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    res = french_to_english(textToTranslate)
    return "Translated text to English:" + " " + str(res)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
