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


python_events = [
    {
        'title': 'First party arrives',
        'start': '2022-12-28 15:00:00',
    },
    {
        'title': 'Shoot the Shit',
        'start': '2022-12-28 16:01:00',
        'end': '2022-12-29 21:00:00',
    },
    {
        'title': 'Second party arrives',
        'start': '2022-12-29 22:30:00',
    },
    {
        'title': 'Park City',
        'start': '2022-12-30 12:00:00',
        'end': '2022-12-30 19:00:00',
    },
    {
        'title': 'Piper Down Pub',
        'start': '2022-12-30 20:00:00',
        'end': '2022-12-30 22:00:00',
    },
    {
        'title': 'Pie Pizzaria',
        'start': '2022-12-31 13:00:00',
        'end': '2022-12-31 15:00:00',
    },
    {
        'title': 'Downtown SLC block',
        'start': '2022-12-31 17:00:00',
        'end': '2022-12-31 20:00:00',
    },
    {
        'title': 'Last Hurrah 2022',
        'start': '2022-12-31 20:00:00',
        'end': '2022-12-31 23:59:59',
    },
    {
        'title': 'East High',
        'start': '2023-01-01 13:00:00',
        'end': '2023-01-01 14:00:00'
    },
    {
        'title': 'Top-Golf',
        'start': '2023-01-01 16:00:00',
        'end': '2023-01-01 18:00:00',
    },
    {
        'title': 'Uinta Brewing Co',
        'start': '2023-01-02 12:00:00',
        'end': '2023-01-02 14:00:00'
    },
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html', events = python_events)

@app.route('/pictures')
def pictures():
    return render_template('pictures.html')