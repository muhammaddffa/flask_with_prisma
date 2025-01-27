from flask import Blueprint, request
from prisma.models import Post
from app.controller.postinganController import PostinganController


posts = Blueprint('postingan', __name__)

@posts.route('/', methods=['GET','POST'])
def getUsers():
    if request.method == "GET":
        return PostinganController.getPostingan()
    # elif request.method == "POST":
    #     return UserController.createUser()