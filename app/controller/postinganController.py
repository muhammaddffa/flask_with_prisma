from flask import jsonify, request
from prisma.models import Post

class PostinganController:
    def getPostingan():
        post = Post.prisma().find_many()
        return {
            "data": [posts.dict() for posts in post ]
        }