# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from project.services.process import process
import cv2
import numpy



@app.route('/')
def start():
    return "Hello Server !!"


@app.route("/uploadImage", methods=["POST"])
def process_image():
    file = request.files['media']
    imgRGB = cv2.imdecode(numpy.fromstring(request.files['media'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
    return process.analyze(imgRGB)
