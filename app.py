from flask import Flask, render_template, send_file
import os
from os import listdir
from os.path import isfile, join
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/return_image',methods=['GET'])
def get_image():
    #onlyfiles = [f for f in listdir(os.getcwd()+"\\imgs\\") if isfile(join(os.getcwd()+"\\imgs\\",f))]
    onlyfiles = [f for f in listdir('./imgs') if isfile(join('./imgs',f))]
    #image_source = "{0}\\imgs\\{1}".format(os.getcwd(),random.choice(onlyfiles))
    image_source = "./imgs/{0}".format(random.choice(onlyfiles))
    return send_file(image_source, mimetype='image/jpg')



if __name__ == '__main__': app.run(debug=True)