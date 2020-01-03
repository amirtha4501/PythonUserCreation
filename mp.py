from flask import Flask, render_template, redirect, request
# import jinja2
import json
# import uuid

mp = Flask(__name__)

# name = request.args.get('name', 'anu')
# print(name)
# Post
# @mp.route('\post')

# Comment
# @mp.route('\comment')

# Like 
# @mp.route('\like')

# Share
# @mp.route('\share')

# Account Creation
# @mp.route('\create')
def createId():
    with open('mp.json','r') as f:
        data = json.load(f)
    a = {
        'fname' : request.args.get('fname'),
        'lname' : request.args.get('lname'),
        'phone' : request.args.get('phone'),
        'mail' : request.args.get('mail'),        
        'password' : request.args.get('password')
    }
    data.update(a)

    with open('mp.json','w') as f:
        json.dump(data, f, indent=4)
    # return redirect('')

# Account login
# @mp.route('\login')
def login():
    with open('mp.json','r') as f:
        data = json.load(f)
        print(data)

    # with open('mp.json','r') as f:
