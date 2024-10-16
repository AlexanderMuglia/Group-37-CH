from flask import Flask, render_template, request, url_for
from flightSearch import bp as flightSearch_bp
from viewFlights import bp as viewFlights_bp

app = Flask(__name__)
app.register_blueprint(flightSearch_bp)
app.register_blueprint(viewFlights_bp)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', user_input=None)

if __name__ == '__main__':
    app.run(debug=True)
