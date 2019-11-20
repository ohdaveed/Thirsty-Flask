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

# countdown show route
@countdowns.route('/<id>', methods=["GET"])
def get_one_countdown(id):

    countdown = models.Countdown.get_by_id(id)

    return jsonify(data={
        'name': countdown.name
        }, status={
        'code': 200,
        'message': "registered users can access more about this"
        }), 200

# update route
# @countdowns.route('/<id>', methods=['PUT'])
# def update_dog(id):
#     payload = request.get.json()

#     countdown = models.Countdown.get_by_id(id)

#     if(countdown.name == 'Jesus'):

#         countdown.name = payload['name'] if 'name' in payload else None

#         countdown.save()

#         countdown_dict = model_to_dict(countdown)

#         return jsonify(data={"Will update"}, status={
#             'code': 200,
#             'message': 'Resource updated successfully'}), 200

#     else:
#         return jsonify(data="Forbidden", status={
#             'code': 403,
#             'message': 'I want this to show until jurgen has users set up'}), 403

@countdowns.route('/<id>', methods=["Delete"])
def delete_countdown(id):

    countdown_to_delete = models.Countdown.get_by_id(id)

    countdown_name = countdown_to_delete.name
    countdown_to_delete.delete_instance()

    return jsonify(data='Countdown delete successfully', status={"code": 200, "message": "{} deleted successfully".format(countdown_name)})


    

