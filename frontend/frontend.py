from flask import Flask, render_template, request, jsonify
import requests

frontend = Flask(__name__)

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    # Use the fully qualified domain name for the backend service
    response = requests.get(f'http://flask-backend-service.backend.svc.cluster.local:5000/api/greet/{name}')
    return response.text

@frontend.route('/names', methods=['GET'])
def names():
    response = requests.get(f'http://flask-backend-service.backend.svc.cluster.local:5000/api/names')
    names_list = response.json()
    return render_template('names.html', names=names_list)

if __name__ == '__main__':
    frontend.run(debug=True, host='0.0.0.0')
