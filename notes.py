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
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/mario',methods=['GET'])
def mario():
    image_source = "{0}\\imgs\\{1}".format(os.getcwd(),random.choice(onlyfiles))
    return "<h1>MARIO</h1> <img src='{0}' width='500' height='600'>".format(image_source)

@app.route('/render')
def renderhtmlpage():
    #image_source = "{0}\\imgs\\{1}".format(os.getcwd(),random.choice(onlyfiles))
    image_source = 'http://127.0.0.1:5000/picture'
    return render_template("index.html", user_image = image_source)

@app.route('/picture',methods=['GET'])
def get_image():
    image_source = "{0}\\imgs\\{1}".format(os.getcwd(),random.choice(onlyfiles))
    return send_file(image_source, mimetype='image/jpg')

@app.route('/jsontest',methods=['GET'])
def jsonData():
    values = {"key":"value","second key":"second value"}
    return values
    
@app.route('/parameter', methods=['GET'])
def paramters_value():
    return request.args.get('username')
app.run()