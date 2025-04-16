fastapi
Question-18:
convert helloj of flask to fastapi


from fastapi import FastAPI , Request
from pydantic import BaseModel
from sqlalchemy import create_engine, text 
from functools import wraps
import os


app = FastAPI()

class Details(BaseModel):
    name:str
    format:str  
@app.post("/helloj/{name}/{fformat}")
def Details_helloj(name:str,fformat:str):
    obj=dict(name=name,format_json=fformat,details="Details added Successfully....")
    return obj
    
@app.post("/helloj")
def create_post_dict(d:Details):
    obj=dict(name=d.name, format=d.format, details="Details were added...")
    return obj 
    


###################################  test_Question18.py##############################################
import requests


    
def sync_post(url,obj):
    return requests.post(url,json=obj)
    
def sync_post_details(url2):
    return requests.post(url2)

    
if __name__ == '__main__':
    url="http://localhost:8000/helloj"
    obj=dict(name="shreya",format="json")
    resp = sync_post(url,obj)
    print(resp.json())
  
 
    url2="http://localhost:8000/helloj/shreya/json"      
    resp=sync_post_details(url2)
    print(resp.json())
    

