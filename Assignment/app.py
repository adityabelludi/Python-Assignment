from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return render_template('index.html', current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        with open('data.json', 'a') as f:
            json.dump({'name': name, 'email': email}, f)
            f.write('\n')
        return redirect(url_for('index'))
    
    
@app.route('/data')
def data():
    with open('data.json', 'r') as f:
        data = [json.loads(line) for line in f]
    return render_template('data.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
