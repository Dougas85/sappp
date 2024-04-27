# app.py

from flask import Flask, render_template, jsonify, send_from_directory
from questions import get_random_question
import os

app = Flask(__name__)

@app.route('/')
def home():
    question = get_random_question()
    return render_template('index.html', question=question['question'], answer=question['answer'])

@app.route('/pdfs/<filename>')
def pdf(filename):
    return send_from_directory(os.path.join(app.root_path, 'pdfs'), filename)

@app.route('/index2')
def index2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
