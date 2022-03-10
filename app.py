try:
    from flask import render_template, redirect, url_for, request, send_from_directory, flash
except:
    print("Not able to import all of the calls needed from the Flask library.")
    

import os
import joblib
from flask import Flask, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

try:
    from PIL import Image
    import PIL.ImageOps
except:
    print("Make sure to pip install Pillow")

import numpy as np
# from matplotlib import pyplot as plt
from cv2 import cv2
# import seaborn as sns


import pandas as pd
import input_processing 
# import predict_modelRF
import image_present 
import image_check
import image_KMeans




#Set up Flask
TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
UPLOAD_FOLDER = os.path.join('static')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key="DisneyQuiz"
app.config['SESSION_COOKIE_SECURE'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
clf = joblib.load(open("Disneymodel.pk1", "rb")) # Load "model.pkl"
print ('Model loaded')
model_columns = joblib.load("model_columns.pk1") # Load "model_columns.pkl"
print ('Model columns loaded')
# UPLOAD_FOLDER = '/static'





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Home page, renders the intro.html template

@app.route('/')
def Disney():
    return render_template('Disney.html', title='Home')

@app.route('/Character_Test',methods=['GET','POST'])
def Character_Test():
    if request.method == 'POST':
        Name = request.form['name']
        Sex = request.form['sex']
        Height= request.form['height']
        Birthday= request.form['birthday']
        Zodiac= request.form['zodiac']
        EC= request.form['EC']
        HC= request.form['HC']
        FC= request.form['FC']

        Name=Name
        N_sex=input_processing.conv_sex(Sex)
        Height=Height
        Birthday=Birthday
        N_Zodiac=input_processing.conv_ZS(Zodiac)
        N_EC=input_processing.conv_EC(EC)
        N_HC=input_processing.conv_HC(HC)
        N_FC=input_processing.conv_FC(FC)

        Features=[N_sex, Height , Birthday, N_Zodiac, N_EC[0], N_EC[1], N_EC[2], N_HC[0], N_HC[1],N_HC[2], N_FC[0],N_FC[1],N_FC[2] ]
        x_feature=[Features]
        prediction = clf.predict(x_feature)
        Result=image_present.image_present(prediction[0])
        image=f"static/C_image/{Result}.png"
        return render_template('CT_results.html', Name=Name, Character=Result, image=image)
    return render_template('Character_Test.html', title='Character_Test')

# Used for uploading pictures
@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static',filename)


@app.route('/image_check', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        Name = request.form['name']
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # if the image is valid, do the following
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # upload=file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("image save")
            # Take the image, make a new one that is inverted
            img = image_check.image_check(filename)
            

        return render_template('image_check_result.html', Name=Name, Character=img, image=filename, image_1=img)
    return render_template('image_check.html', title='image_check')


@app.route('/Disney_search', methods=['GET', 'POST'])
def Disney_search():

    return render_template('Disney_search.html', title='KNOWSMORE')


@app.route('/paintingroom', methods=['GET', 'POST'])
def paintingroom():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # if the image is valid, do the following
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # upload=file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # Take the image, make a new one that is inverted
            img = image_KMeans.color_quantization(filename)
            new_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) 
            cv2.imwrite(f'static/new_{filename}',new_image)
            new_image=(f'new_{filename}')

        return render_template('PTR_result.html', image=filename, image_1= new_image)
    return render_template('paintingroom.html', title='colorquantization')




           
           
if __name__ == "__main__":
    app.run(debug=True)