# from flask import jsonify, request
# from prisma.models import User

# class UserController:
#     def getUser():
#         users = User.prisma().find_many(include={'posts': True})
#         return {
#         "data": [user.dict() for user in users]
#         }

#     def createUser():
#         data = request.json

#         if data is None:
#         return

#         name = data.get('name')
#         email = data.get('email')

#         if name is None or email is None:
#         return {"error": "You need to provide name and email"}

#         user = User.prisma().create(data={'email': email, 'name': name})

#         return dict(user)