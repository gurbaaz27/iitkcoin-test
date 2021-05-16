from application import app
from flask import Flask, request

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return "Welcome to IITK Coin lite :/ <br>For dummy data, there are 1000 roll numbers.<br> Each roll no has coins double their value of roll no.<br> Head over to <a href='/coins'>coins</a>"


@app.route('/coins', methods=['GET','POST'])
def coins():
    hashmap = {}

    for i in range(1001):
        hashmap[i] = 2*i

    if request.method == 'POST':
        rollno = request.form.get('rollno')
        response = {
            'coins': hashmap[int(rollno)]
        }

        return response
    
    return '''
            <form method="POST">
               <div><label>Roll no: <input type="text" name="rollno"></label></div>
               <input type="submit" value="Submit">
           </form>
            '''