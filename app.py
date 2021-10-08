from flask import Flask, request, jsonify
from config.conf import settings
from utils.sync import sync_with_storage
app = Flask(__name__)


@app.route('/')
def home():
    return 'OK'


@app.route('/sync', methods=['POST'])
def sync():
    data = request.json
    sync_with_storage(data)
    return jsonify({'result': 'OK'})


def run():
    app.run(host='0.0.0.0',
            port=settings['port'])


def debug():
    app.run(host='0.0.0.0',
            port='5000')


if __name__ == '__main__':
    run()
