import models

from flask import jsonify, request, Blueprint

from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

countdowns = Blueprint("countdowns", "countdowns")

# @countdowns.route("/", methods=["GET"])
# def get_all_countdowns():
#     return("testing the countdown route")

# index route
@countdowns.route("/", methods=["GET"])
def countdowns_index():

    try:
        # will hit here Jurgen makes the users side

        return jsonify(data={}, status={"code": 200, "message": "Success"}), 200

    except models.DoesNotExist:
        return (
            jsonify(
                data={},
                status={
                    "code": 401,
                    "message": "making a placehold until Jurgen creates users.py",
                },
            ),
            401,
        )


#create countdown route
@countdowns.route("/", methods=["POST"])
def create_countdown():
    payload = request.get_json()

    countdown = models.Countdown.create(
        name=payload["name"],
        # image=payload["image"],
        # # timer=payload["timer"],
        # # owner=current_user.id,
        
    )

    print(model_to_dict(countdown), "model_to_dict")
    countdown_dict = model_to_dict(countdown)

    return jsonify(data=countdown_dict, status={"code": 201, "message": "Success"}), 201
