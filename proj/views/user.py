from flask import Blueprint, render_template, request, make_response,jsonify
import sys, os, json
# from proj.models.model import *

bp_user = Blueprint('bp_user', __name__)


@bp_user.route('/list', methods=['GET'])
def list():
    data = []

    try:
        # use = User(name="SS",age="ff",date_birth=None,gender="SSS")
        # db.session.add(use)
        # db.session.commit()
        item = dict()
        item['name'] = "Zulkamaluddin Bin Pakharuddin"
        item['age'] = "ff"
        item['birth'] = "24 August 2002"

        data.append(item)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        msg = exc_obj, fname, "Line number : ", exc_tb.tb_lineno
        print(msg)
    return jsonify(data)