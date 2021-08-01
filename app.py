import logging

from flask import Flask, jsonify

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


@app.route("/")
def hello():
    app.logger.info('hello request successful')
    return "Hello World!"


@app.route('/status')
def status():
    app.logger.info('Status request successful')
    return jsonify({
        'result': 'OK - healthy'
    })


@app.route('/metrics')
def metrics():
    app.logger.info('Metrics request successful')
    return jsonify({
        'status': 'success',
        'code': 0,
        'data': {
            'UserCount': 140,
            'UserCountActive': 23
        }
    })


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
