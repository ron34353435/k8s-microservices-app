from flask import Flask, request, send_from_directory, render_template, jsonify

#flask app object
app = Flask(__name__)

#json format data about products
pipeline =  { "product":"pipeline", "by":"Mario", "price":"30",\
"description":"We sell original pipeline from Mario"}

python = { "product":"python", "by":"Guido van Rossum", "price":"200",\
"description":"Adopt a python"}

packet = { "product":"packet", "by":"Noy Krief", "price":"10",\
"description":"This product will help you stop smoking packets"}

docker = { "product":"docker", "by":"Dudu Faruk", "price":"0",\
"description":"bakaba noder malshinim docker"}

bucket = { "product":"bucket", "by":"china", "price":"20",\
"description":"Over drinking is unhealthy."}

cloud = { "product":"cloud", "by":"Neo", "price":"100",\
"description":"We offer sell your soul to matrix cloud."}

wireshark = { "product":"wireshark", "by":"nahshoof", "price":"300",\
"description":"Adopt baby shark"}

tux = { "product":"tux", "by":"Elin & Alin", "price":"100",\
"description":"Buy evil tux who destroy windows"}

#get request to http://ip:port/<path>
#return data of relevent product
@app.route('/<path:path>')
def product(path):
    if path == "pipeline":
        return jsonify(pipeline)
    elif path == "python":
        return jsonify(python)
    elif path == "packet":
        return jsonify(packet)
    elif path == "docker":
        return jsonify(docker)
    elif path == "bucket":
        return jsonify(bucket)
    elif path == "cloud":
        return jsonify(cloud)
    elif path == "wireshark":
        return jsonify(wireshark)
    elif path == "tux":
        return jsonify(tux)
    else:
        return "error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

