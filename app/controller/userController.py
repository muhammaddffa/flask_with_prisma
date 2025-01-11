from flask import jsonify, request
from prisma.models import User

class UserController:
    def getUser():
        users = User.prisma().find_many(include={'posts': True})
        return {
        "data": [user.dict() for user in users]
        }
    def createUser():
        data = request.get_json()

        if not data or 'name' not in 'email' not in data:
            return jsonify ({
                "message": "name and emai are required"
            }), 400

        user = User.prisma().create(
            data = {
                "name": data["name"],
                "email": data["email"]
            }
        )

        return jsonify(user.dict()),201