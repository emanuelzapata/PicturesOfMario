from flask import Flask, render_template, send_file, request, jsonify
import os
from os import listdir
from os.path import isfile, join
import random
import json 

app = Flask(__name__)

def generateJSON():
    jasonVals = []
    for i in range(63):
        print(i+1)
        jasonVals.append({
                "imageID": i+1,
                "rarity": 10,
                "era": "post weight loss",
                "mediatype":"jpg"
        })
    with open('marios.json', 'w') as outfile:
        json.dump(jasonVals, outfile)
marios = json.load(open("marios.json"))

@app.route('/')
def index():
    #generateJSON()
    #print(marios['45'])
    return render_template('index.html', passed="variablename")

@app.route('/api/v1/sample')
def sample():
    onlyfiles = [f for f in listdir('./imgs') if isfile(join('./imgs',f))]
    image_source = "./imgs/{0}".format(random.choice(onlyfiles))
    return send_file(image_source, mimetype='image/jpg')

@app.route('/api/v1/get_mario',methods=['GET'])
def return_mario():
    marios = json.load(open("marios.json"))
    mario = random.choice(marios)
    return jsonify(mario)

@app.route('/api/v1/return_media',methods=['GET'])
def return_media():
    image_id = request.args.get('id')
    image_source = "./imgs/{0}.{1}".format(image_id,marios[image_id]['mediatype'])
    return send_file(image_source)

if __name__ == '__main__': app.run(debug=True)