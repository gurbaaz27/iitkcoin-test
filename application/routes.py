from application import app
from flask import Flask, request
from random import random

hashmap = {}

for i in range(10001):
    hashmap[i] = int(random()*1000)


@app.errorhandler(404)
def page_not_found(e):
    return "Error 404 Nibba! Move back where you came from!<br><br>Or head to <a href='/'>home</a>"


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return "<h2>Welcome to IITK Coin lite :)</h2><br>For dummy data, there are 10000 roll numbers, numbered 1 to 10000.<br> Each roll no has random number of  coins.<br>If you want to use curl and interact with the endpoint <b>/coin</b>, enter in terminal <br> <code><pre>curl -d '{\"rollno\": <rollno>}' -H 'Content-Type: application/json' localhost:8000/coins</pre></code><br><b>Additional:</b> If you want to interact POST method via rather an html form, head over to endpoint <b>/coins-form</b> <a href='/coins-form'>here</a>."


@app.route('/coins', methods=['POST'])
def coins():
    request_data = request.get_json()

    rollno = 0
    if request_data:
        if 'rollno' in request_data:
            rollno = int(request_data['rollno'])
    
    if rollno > 10000 or rollno < 1:
        response = {
                'coins': "Rollno out of allocated range (10000)"
        }
    else:
        response = {
                'coins': hashmap[rollno]
        }

    return response


@app.route('/coins-form', methods=['GET','POST'])
def coinsform():
    if request.method == 'POST':
        rollno = int(request.form.get('rollno'))
        if rollno > 10000 or rollno < 1:
            response = {
                'coins': "Rollno out of allocated range (10000)"
            }
        else:
            response = {
                'coins': hashmap[rollno]
            }

        return response
        
    return '''
            <h2>Check your coins</h2><br>
            <form method="POST">
            <div><label>Roll no: <input type="text" name="rollno" placeholder="Enter your roll no."></label></div><br>
            <input type="submit" value="Submit">
            </form>
            <br>
            Back to <a href='/'>home</a>
            '''