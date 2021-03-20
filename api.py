import flask
from flask import send_file, render_template, request
from os import listdir
from os.path import isfile, join
import os
import random 
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def edit_json(data):
    for image in data:
        print(image["imageID"])

@app.route('/api/v1/get_image_by_id',methods=['GET'])
def get_image_by_id():
    image_ID = request.args.get('id')
    return image_ID

@app.route('/api/v1/get_data',methods=['GET'])
def get_data():
    #edit_json(json.load(open("data.json")))
    return {"image":1}
    
def main():
    app.run()

if __name__=="__main__":
    main()