from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about-us')
def about_us():
    return render_template('about-us.html')


@app.route('/main-program')
def main_program():
    return render_template('main-program.html')


if __name__ == '__main__':
    app.run()
