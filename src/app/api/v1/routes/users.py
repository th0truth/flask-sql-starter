from flask import Blueprint, jsonify, request

from app.core.schema import UserBase
from app.core.security import Hash
from app.main import db

bp = Blueprint("Users", __name__)


@bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json() or {}

    username = data.get("username")
    plain_password = data.get("password", "")

    if not plain_password:
        return jsonify({"message": "Password required"}), 409

    email = data.get("email")

    if not username or not email:
        return jsonify({"message": "Please provide username and email"}), 400

    existing_user = db.session.scalars(
        db.select(UserBase).where(
            (UserBase.username == username) | (UserBase.email == email)
        )
    ).first()

    if existing_user:
        return jsonify({"message": "User already exists"}), 409

    new_user = UserBase(
        username=username, email=email, password_hash=Hash.hash(plain_password)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(
        {"id": new_user.id, "username": new_user.username, "email": new_user.email}
    ), 201


@bp.route("/all", methods=["GET"])
def get_all_users():
    users = db.session.scalars(db.select(UserBase)).all()

    return jsonify(
        [
            {
                "id": u.id,
                "username": u.username,
                "email": u.email,
                "hash_password": u.password_hash,
            }
            for u in users
        ]
    ), 200
