from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():

    quart = pd.read_excel('./milano_housing_02_2_23.xlsx')
    dropped = quart.drop_duplicates().sort_values("neighborhood")
    table = dropped.to_html()
    return render_template('es3OUT.html', table = table)
 





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)