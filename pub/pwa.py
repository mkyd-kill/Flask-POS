from flask import Blueprint, send_from_directory, make_response

progressive = Blueprint('pwa', __name__, url_prefix='')

@progressive.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@progressive.route('/service_worker.js')
def worker():
    response = make_response(send_from_directory('static', 'service_worker.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response