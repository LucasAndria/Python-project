from flask import Flask, render_template,  request, url_for, flash, redirect
from models.produitModel import *

app = Flask(__name__) #instance d'application Flask

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/produit')
def produit():
    cursor = listProduit()
    return render_template('produit.html', produits = cursor)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=9000)
