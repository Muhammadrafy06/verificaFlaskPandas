from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('es4IN.html')


@app.route('/es4')
def es1():
    inputStr = request.args.get("quartiere")
    quart = pd.read_excel('./milano_housing_02_2_23.xlsx')
    risultato = quart[quart["neighborhood"] == inputStr].mean()[["price"]]
    table = risultato.to_html()
    return render_template('es4OUT.html', table = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)