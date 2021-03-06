import models

from flask import jsonify, request, Blueprint

from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

import datetime
import time


countdowns = Blueprint("countdowns", "countdowns")

# index route
@countdowns.route("/", methods=["GET"])
@login_required
def countdowns_index():

    try:
        this_user_countdown_instances = models.Countdown.select().where(
            models.Countdown.owner_id == current_user.id
        )

        this_users_countdown_dicts = [
            model_to_dict(countdown) for countdown in this_user_countdown_instances
        ]

        this_users_countdown_dicts_no_password = [
            countdown["owner"].pop("password", None)
            for countdown in this_users_countdown_dicts
        ]

        return (
            jsonify(
                data=this_users_countdown_dicts,
                status={"code": 200, "message": "Success"},
            ),
            200,
        )

    except models.DoesNotExist:
        return (
            jsonify(
                data={},
                status={"code": 401, "message": "Error getting the resources", },
            ),
            401,
        )


# create countdown route
@countdowns.route("/", methods=["POST"])
@login_required
def create_countdown():
    payload = request.get_json()
    countdown = models.Countdown.create(
        name=payload["name"],
        image=payload["image"],
        timer=payload["timer"],
        owner=current_user.id,
    )

    print(model_to_dict(countdown), "model_to_dict")
    countdown_dict = model_to_dict(countdown)

    countdown_dict["owner"].pop("password")

    return jsonify(data=countdown_dict, status={"code": 201, "message": "Success"}), 201


# countdown show route
@countdowns.route("/<id>", methods=["GET"])
def get_one_countdown(id):

    countdown = models.Countdown.get_by_id(id)

    if not current_user.is_authenticated:
        return (
            jsonify(
                data={"name": countdown.name, "timer": countdown.timer},
                status={
                    "code": 200,
                    "message": "registered users can access more about this",
                },
            ),
            200,
        )

    else:
        countdown_dict = model_to_dict(countdown)
        countdown_dict["owner"].pop("password")

        if countdown.owner_id != current_user.id:
            countdown_dict.pop("created_at")

        return (
            jsonify(
                data=countdown_dict,
                status={
                    "code": 200,
                    "message": "Found countdown with id {}".format(countdown.id),
                },
            ),
            200,
        )


# update route
@countdowns.route("/<id>", methods=["PUT"])
def update_countdown(id):

    payload = request.get_json()

    countdown = models.Countdown.get_by_id(id)

    countdown.name = payload["name"] if "name" in payload else None

    countdown.image = payload["image"] if "image" in payload else None

    countdown.timer = payload["timer"] if "timer" in payload else None

    countdown.save()

    countdown_dict = model_to_dict(countdown)

    return (
        jsonify(
            data=countdown_dict,
            status={"code": 200, "message": "Resource updated successfully"},
        ),
        200,
    )


# delete route
@countdowns.route("/<id>", methods=["Delete"])
def delete_countdown(id):

    countdown_to_delete = models.Countdown.get_by_id(id)

    countdown_name = countdown_to_delete.name
    countdown_to_delete.delete_instance()

    return jsonify(
        data="Countdown delete successfully",
        status={
            "code": 200,
            "message": "{} deleted successfully".format(countdown_name),
        },
    )


# show route
@countdowns.route("/countdowns/all", methods={"GET"})
def show_countdowns_all_users():
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


# water plant
@countdowns.route("/updatetime/<id>", methods={"PUT"})
def countdown_last_watered(id):

    now = time.time()

    countdown = models.Countdown.get_by_id(id)

    countdown.last_watered = now

    countdown.save()

    countdown = models.Countdown.get_by_id(id)
    countdown_dict = model_to_dict(countdown)

    return (
        jsonify(
            data=countdown_dict,
            status={"code": 200, "message": "Resource updated successfully"},
        ),
        200,
    )


# set last_watered to be now
