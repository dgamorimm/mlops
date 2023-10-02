from flask import Flask
from textblob import TextBlob
from translate import Translator
from rich import print
import joblib
import os

translator= Translator(from_lang='pt', to_lang='en')

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

@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    modelo = joblib.load(os.path.join(os.path.dirname(__file__),'model/modelo-houses-price.pkl'))
    preco = float(modelo.predict([[tamanho]]))
    return f"Cotação: R${preco:,.2f}"

app.run(debug=True)