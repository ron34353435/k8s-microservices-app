from flask import Flask, request, send_from_directory, render_template, jsonify
import os

os.environ["APP_FILE"] = "catalog.py"

#flask app object
app = Flask(__name__)

#json format data about products
products =  { "product_1":"Pipeline", "product_2":"Python", "product_3":"Packet",\
"product_4":"Docker","product_5":"Bucket","product_6":"Cloud",\
"product_7":"wireSHARK","product_8":"Tux"}

@app.route('/')
def catalog():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
