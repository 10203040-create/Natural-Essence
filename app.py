
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/investigacion')
def investigacion():
    return render_template('investigacion.html')

@app.route('/elaboracion')
def elaboracion():
    return render_template('elaboracion.html')

@app.route('/producto')
def producto():
    return render_template('producto.html')


@app.route('/comparativa')
def comparativa():
    return render_template('comparativa.html')
@app.route('/carteles')
def carteles():
    return render_template('carteles.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)