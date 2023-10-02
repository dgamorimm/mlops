from flask import Flask, request, jsonify
from textblob import TextBlob
from translate import Translator
from rich import print
from collections import OrderedDict
import joblib
import os

translator= Translator(from_lang='pt', to_lang='en')

# Defina a ordem desejada das chaves
sort_key = ["Tamanho", "Ano", "Garagem"]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Minha primeira API'

@app.route('/sentimento/<frase>')
def sentimento(frase):
    translation = translator.translate(frase)
    print(translation)
    tb = TextBlob(translation)
    polarity = tb.sentiment.polarity
    return f'Polaridade: {polarity:.0%}'

@app.route('/cotacao/', methods=['POST'])
def cotacao():
    payload = request.get_json()
    sorted_key = OrderedDict((key, payload[key]) for key in sort_key)
    data = list(sorted_key.values())
    modelo = joblib.load(os.path.join(os.path.dirname(__file__),'model/modelo-houses-price.pkl'))
    preco = float(modelo.predict([data]))
    return jsonify(preco=f"R${preco:,.2f}")

app.run(debug=True)