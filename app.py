from flask import Flask, render_template, send_file, request, jsonify
import os
from os import listdir
from os.path import isfile, join
import random
import json 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', passed="variablename")

@app.route('/generate_json')
def generate_json():
    data = {}
    data['marios'] = []
    for i in range(44):
        data['marios'].append(  {
            "imageID": i+1,
            "rarity": 10,
            "era": "post weight loss"
        })
    with open('marios.json', 'w') as outfile:
        json.dump(data, outfile)
    return "done"

@app.route('/sample')
def sample():
    return send_file('./imgs/21.jpg', mimetype='image/jpg')

@app.route('/get_mario',methods=['GET'])
def return_mario():
    marios = json.load(open("marios.json"))
    mario = random.choice(marios)
    return jsonify(mario)

@app.route('/api/v1/return_image',methods=['GET'])
def return_image():
    image_id = request.args.get('id')
    #onlyfiles = [f for f in listdir('./imgs') if isfile(join('./imgs',f))]
    image_source = "./imgs/{0}.jpg".format(image_id)
    return send_file(image_source, mimetype='image/jpg')

if __name__ == '__main__': app.run(debug=True)