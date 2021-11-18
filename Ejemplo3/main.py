from flask import Flask,request,abort

app = Flask(__name__)

usuarios=[1,2,3,4,5]

@app.route('/')
def index():
    if request.method == 'GET':
        return "GET executed"
    if request.method == 'POST':
        return "POST executed"
    if request.method == 'DELETE':
        return "DELETE executed"
    else:
        abort(405,description="Method not allowed")
    return 'Web App with Python Flask!'

@app.route('/users/1', methods = ['GET', 'POST', 'DELETE'])
def getuser(user_id):
    if request.method == 'GET':
        return "GET executed"
    if request.method == 'POST':
        return "POST executed"
    if request.method == 'DELETE':
        return "DELETE executed"
    else:
        abort(405,description="Method not allowed")

app.run(host='0.0.0.0', port=5001)
