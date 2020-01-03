from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Account Creation
@app.route('/create',methods=['GET','POST'])
def create_id():
    input_data = request.get_json()
    with open('register.json','r+') as f:
        data = json.load(f)

    a = {
        'fname' : input_data.get('fname'),
        'lname' : input_data.get('lname'),
        'phone' : input_data.get('phone'),
        'mail' : input_data.get('mail'),        
        'password' : input_data.get('password')
    }

    data['members'].append(a)
    
    c = 0
    for i in data['members']:
        id = {'user_id' : c+1}
        i.update(id)
        c = c+1
    # print(data)
    with open('register.json','w') as f:
        json.dump(data, f, indent=4)

    return 'Done'


# Login
@app.route('/login', methods=['POST'])
def login():

    input_data = request.get_json()
    with open("register.json","r") as f:
        data = json.load(f)

        b = {
            'fname' : input_data.get('fname'),      
            'password' : input_data.get('password')
        }

        flag = False
        for li in data['members']: # accesses each dict in a list that is a value of another dict in register.json

            # compares the name & password of user's input and register.json file
            if li['fname'] == b['fname'] and li['password'] == b['password']: 

                with open('login.json','r+') as f:
                    data = json.load(f) # obtains details in login.json
                    is_existing = False
        
                    for row in data['logged_users']: # accesses each dict in a list that is a value of another dict in login.json
                        
                        # compares the user's input fname & password to each dicts of login.json's fname & password 
                        if b['fname'] == row['fname'] and b['password'] == row['password']: 
                            is_existing = True
            
                        else: # if id is already in login.json, then nothing happens
                            print("You're already logged in.")
            
                    if not is_existing:
                        # If id of the dict is not in the login.json, then appends the user's dict
                        data['logged_users'].append(li)

        with open('login.json','w') as f: # opening  login.json 
                json.dump(data,f,indent=4)
                process = "You're logged in successfully"
                flag = True
    

        if flag == False:
            process = "User name or password is incorrect."

    return process


app.run(host='0.0.0.0',port=6000,debug=True)


# Post
# @mp.route('\post')









# Comment
# @mp.route('\comment')

# Like 
# @mp.route('\like')

# Share
# @mp.route('\share')
