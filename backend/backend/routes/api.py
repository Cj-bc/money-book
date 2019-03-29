from flask import Blueprint, jsonify, request, current_app

bp = Blueprint(__name__, 'api')


@bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})
