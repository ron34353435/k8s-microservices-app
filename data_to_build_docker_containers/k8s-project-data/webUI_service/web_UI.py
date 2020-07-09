from flask import Flask, request, send_from_directory, render_template
import requests
import time
import os


#set flask object. shopfiles is the name of dir of tempaltes.
app = Flask(__name__, template_folder="shopfiles")

#In future it will be name of service
PRODUCT_ENV = os.environ.get('PRODUCT')
CATALOG_ENV = os.environ.get('CATALOG')
PRODUCT_URL = r"http://{}/{}".format(PRODUCT_ENV,"{}")
print(PRODUCT_URL)
CATALOG_URL = r"http://{}/".format(CATALOG_ENV)
print(CATALOG_URL)

def render_product_by_service(product):
    """
    make http GET request to product service.
    get json format data.
    render data to html page.
    """
    r = requests.get(url = PRODUCT_URL.format(product))
    data = r.json()
    return render_template("productpage.html",
                            product=data["product"], by=data["by"],
                            price=data["price"], description=data["description"])

def render_catalog_by_service():
    """
    make http GET request to catalog service.
    get json format data.
    render data to html page.
    """
    r = requests.get(url = CATALOG_URL)
    data = r.json()
    return render_template("index.html",
                           product_1=data["product_1"], product_2=data["product_2"],
                           product_3=data["product_3"], product_4=data["product_4"],
                           product_5=data["product_5"], product_6=data["product_6"],
                           product_7=data["product_7"], product_8=data["product_8"])

@app.route('/')
def catalog():
    """
    return main catalog page.
    index.html in shopfiles path
    """
    try:
        return render_catalog_by_service()
    except:
        return render_template("index.html",
                           product_1="error", product_2="error",
                           product_3="error", product_4="error",
                           product_5="error", product_6="error",
                           product_7="error", product_8="error")

@app.route('/css/<path:path>')
def send_css(path):
    """
    return all css pages
    """
    return send_from_directory('./shopfiles/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    """
    return all js pages
    """
    return send_from_directory('./shopfiles/js', path)

@app.route('/images/<path:path>')
def send_images(path):
    """
    return all images
    """
    return send_from_directory('./shopfiles/images/', path)

@app.route('/product/<path:path>')
def product(path):
    """
    render product page from productpage.html
    pictures taken from images/<product>/1-4.png
    """
    try:
        return render_product_by_service(path)
    except:
        return render_template("productpage.html",
                                product="error", by="error",
                                price="error", description="error")
            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
