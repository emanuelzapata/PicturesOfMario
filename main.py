import flask
from flask import send_file, render_template, request
from os import listdir
from os.path import isfile, join
import os
import random 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


onlyfiles = [f for f in listdir('E:/Projects/Python_Projects/PicturesOfMario/imgs/') if isfile(join('E:/Projects/Python_Projects/PicturesOfMario/imgs/', f))]

@app.route('/', methods=['GET'])
def home():
    json_data = {
        "imageID":"{0}".format(random.choice(onlyfiles)[:-4]),
        "rarity":"1",
        "era":"Young Mario"
    }
    return json_data

@app.route('/mariodata',methods=['GET'])
def mario_data():
    json_data = {
        "imageID":"{0}".format(random.choice(onlyfiles)[:-4]),
        "rarity":"1",
        "era":"Young Mario"
    }
    return json_data

@app.route('/GetImageById',methods=['GET'])
def get_image_by_id():
    image_ID = request.args.get('ID')
    image_source = "{0}\\imgs\\{1}.jpg".format(os.getcwd(),image_ID)
    try:
        return send_file(image_source, mimetype='image/jpg')
    except:
        return "IMAGE NOT FOUND"
app.run()