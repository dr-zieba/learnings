from flask import Flask, render_template
from display import display

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="secret")

test_config = None

if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
else:
    app.config.from_mapping(test_config)

@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

@app.route('/show')
def show():
    return render_template('coins_index.html', symbols=display())

@app.route('/show/<symbol>')
def show_details(symbol):
    return render_template('coin_show.html', symbol=symbol)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)


