# Question-11:
# Weather mock API 
# format comes from below endpoint 
    # Parse format, if xml, show xml, 
    # if none, show json 
    # Put all random temp 
    # City name may change based on PATH param 
    # (currently not implemented in demo api endpoint)

# DO the same as 
# http://notepadfromdas.pythonanywhere.com/w/mumbai?format=xml
# http://notepadfromdas.pythonanywhere.com/w/mumbai

from flask import Flask, jsonify, g , request,session
import os
import random

from datetime import datetime,timedelta
from random import choices
current_day='Mon'
app = Flask(__name__)
app.secret_key=b"jhhhhhhhhhhhhhhhhhhhsdbn"

def find_day(c_day):
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    current_day =c_day
    index = days.index(current_day)
    next_day = days[(index + 1) % len(days)]
    return next_day

def find_date(i):
    start_date=datetime(2025, 4, 19)
    current_date= start_date + timedelta(days=i)
    format_date=current_date.strftime('%d %b %Y')
    return format_date
    
def weather_data_generation(city):
    global current_day
    weather_dict={}
    weather_dict['city']=city
    weather_dict['pubDate']=datetime(2025, 4, 19)
    
    weather_dict['condition']=dict(code= random.randint(20,50),date=datetime(2025, 4, 19),
    temp=round(random.uniform(15.0, 40.0), 2),
    text = random.choice(['Mostly Cloudy', 'Cloudy', 'Partly Cloudy', 'Mostly Sunny', 'Breezy','Clear']))
    no_of_times=10
    
    weather_list=[]
    for i in range(no_of_times):
        weather_list.append(dict(code=random.randint(20,40),
        date=find_date(i),day=find_day(current_day),high=random.randint(20,30),low=random.randint(15,20),
        text = random.choice(['Mostly Cloudy', 'Cloudy', 'Partly Cloudy', 'Mostly Sunny', 'Breezy','Clear'])))
    weather_dict['forecast']=weather_list
    
    return  weather_dict
    
@app.route("/weather/<string:city>",methods=['GET'])
def weather(city):
    data = weather_data_generation(city)
    return jsonify(data)   

if __name__=='__main__':
    app.run()


"""""""""
commands in cmd

import requests
sess = requests.Session() 
weather_url = ("http://localhost:5000/weather/mumbai", 
            sess.get,
            {})
url, method, data = weather_url  
r = method(url, **data)
print(r.json()) 
sess.close()

"""

