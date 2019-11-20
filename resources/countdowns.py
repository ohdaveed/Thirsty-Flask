import models

from flask import jsonify, request, Blueprint

from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

countdowns = Blueprint("countdowns", "countdowns")

# @countdowns.route("/", methods=["GET"])
# def get_all_countdowns():
#     return("testing the countdown route")

@countdowns.route("/", methods=['GET'])
def countdowns_index():


    try:
        # will hit here Jurgen makes the users side

        return jsonify(data={}, status={
            "code": 200,
            "message": "Success"
            }), 200

    except models.DoesNotExist:
        return jsonify(data={}, status={
            "code": 401,
            "message": "making a placehold until Jurgen creates users.py"
            }), 401

