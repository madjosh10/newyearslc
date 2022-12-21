from app import app
from flask import render_template, redirect, url_for
# from models import Task
# from datetime import datetime

# import forms
# import models

# nav.Bar('top', [
#     nav.Item('Home', 'index'),
#     nav.Item
# ])


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')