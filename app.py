from flask import Flask, render_template, send_file
import os
from os import listdir
from os.path import isfile, join
import random

app = Flask(__name__)

onlyfiles = [f for f in listdir('E:/Projects/Python_Projects/PicturesOfMario/imgs/') if isfile(join('E:/Projects/Python_Projects/PicturesOfMario/imgs/', f))]
print(os.getcwd())
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/marioname')
def marion_name():
    return "mario"

@app.route('/api/v1/return_image',methods=['GET'])
def get_image():
    onlyfiles = [f for f in listdir(os.getcwd()+"\\imgs\\") if isfile(join(os.getcwd()+"\\imgs\\",f))]
    image_source = "{0}\\imgs\\{1}".format(os.getcwd(),random.choice(onlyfiles))
    return send_file(image_source, mimetype='image/jpg')



if __name__ == '__main__': app.run(debug=True)