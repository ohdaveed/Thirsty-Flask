import models

from flask import jsonify, request, Blueprint

from playhouse.shortcuts import model_to_dict

countdowns = Blueprint("countdowns", "countdowns")

@countdowns.route("/", methods=["GET"])
def get_all_countdowns():
    return("testing the countdown route")