from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html' , title = 'Home Page')

@app.route('/docs')
def docs():
    return render_template('docs.html' , title = 'Docs')


if __name__ == '__main__' :
    app.run(debug = True)

