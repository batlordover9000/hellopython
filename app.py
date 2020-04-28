from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    #  lstheros = ['Batman', 'Superman', 'Wonder Woman', 'Kabbo']
    #  return render_template('index.html', heros=lstheros)
    #  return redirect(url_for('about'))
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/css')
def css():
    return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True)
