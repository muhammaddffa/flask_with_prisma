from flask import Flask
from prisma import Prisma, register
from app.routes.userRoute import users
from app.routes.postinganRoute import posts

db= Prisma()
db.connect()
register(db)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return {
    "message": "API IS AWESOME 🎉"
  }

app.register_blueprint(users, url_prefix='/user')
app.register_blueprint(posts, url_prefix= '/post')

if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')