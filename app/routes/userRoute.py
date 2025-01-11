# from app import response, app, db
# from flask import jsonify, request
# from prisma.models import User

from flask import Blueprint, request
from prisma.models import User
from app.controller.userController import UserController


users = Blueprint('user', __name__)

@users.route('/', methods=['GET','POST'])
def getUsers():
    if request.method == "GET":
        return UserController.getUser()
    elif request.method == "POST":
        return UserController.createUser()