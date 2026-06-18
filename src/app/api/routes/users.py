from app.main import app

@app.route('/users', methods=["GET"])
def get_users():
  return ["user_1", "user_2"]
