"""Take the parameters from router, parse them, execute and return the results."""
import json

from flask import request, jsonify, Blueprint

from api.models.cunik import CunikApi

bp = Blueprint('cunik', __name__)


@bp.route('/create', methods=['POST'])
def create():
    image_name = request.form.get('image_name')
    params = {}
    params['ipv4_addr'] = request.form.get('ipv4_addr')
    print(image_name, params, '=======================')
    return CunikApi.create(image_name=image_name, params=params)


@bp.route('/list', methods=['GET'])
def list():
    return json.dumps(CunikApi.list())


@bp.route('/info', methods=['POST'])
def info():
    cid = request.form.get('cid')
    return CunikApi.info(cid=cid)


@bp.route('/stop', methods=['POST'])
def stop():
    cid = request.form.get('cid')
    return CunikApi.stop(cid=cid)


@bp.route('/remove', methods=['POST'])
def remove():
    cid = request.form.get('cid')
    return CunikApi.remove(cid=cid)
