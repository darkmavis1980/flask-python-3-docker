from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')