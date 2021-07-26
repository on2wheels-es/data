import flask
import pandas as pd
import datetime
import random
from flask import request, jsonify

df = pd.read_csv('weekly_weather.csv')

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>On2wheels weather API</h1>
<p>A prototype weather API for destination selection based on the CWI.</p>'''


@app.route('/api/weather', methods=['GET'])
def api_all():
    df = pd.read_csv('weekly_weather.csv')
    if 'mm' in request.args:
        month = int(request.args['mm'])
    if 'dd' in request.args:
        day = int(request.args['dd'])
    if 'ccaa' in request.args:
        ccaa_list = eval(request.args['ccaa'])
    weekNumber = str(datetime.date(2021, month, day).isocalendar()[1])
    if len(ccaa_list) == 1: 
        response = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']][df['CCAA_ID'] == ccaa_list[0]].sort_values('w'+weekNumber, ascending=False).head(5)['town_ID'].tolist()
    elif len(ccaa_list) == 15: 
        response = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']].sort_values('w'+weekNumber, ascending=False).head(5)['town_ID'].tolist()
    else: 
        a = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']][df['CCAA_ID'] == random.choice(ccaa_list)].sort_values('w'+weekNumber, ascending=False).head(3)['town_ID'].tolist()[0:3]
        b = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']][df['CCAA_ID'] == random.choice(ccaa_list)].sort_values('w'+weekNumber, ascending=False).head(3)['town_ID'].tolist()[0:3]
        c = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']][df['CCAA_ID'] == random.choice(ccaa_list)].sort_values('w'+weekNumber, ascending=False).head(3)['town_ID'].tolist()[0:3]
        d = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']][df['CCAA_ID'] == random.choice(ccaa_list)].sort_values('w'+weekNumber, ascending=False).head(3)['town_ID'].tolist()[0:3]
        e = df[['w'+weekNumber, 'town_ID', 'CCAA_ID']][df['CCAA_ID'] == random.choice(ccaa_list)].sort_values('w'+weekNumber, ascending=False).head(3)['town_ID'].tolist()[0:3]
        response = []
        for n in [a,b,c,d,e]:
            for i in n:
                response.append(i)
        response = list(set(response))[0:5]
                
    return jsonify({'destination': response})

app.run()