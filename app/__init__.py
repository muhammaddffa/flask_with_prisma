from flask import Flask
from prisma import Prisma, register
from app.routes.userRoute import user_blueprint

db= Prisma()
db.connect()
register(db)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return {
    "ping": "pong 🎉"
  }

app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')