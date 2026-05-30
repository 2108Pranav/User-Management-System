from flask.views import MethodView
from flask import request, jsonify
from models import User
from db import mysql_db

class CreateAndRetrievesUserResource(MethodView):
    def get(self):
        try:
            data = User.query.all()
            data = [{"id": user.id, "name": user.name, "email": user.email, "number": user.number} for user in data]
            return jsonify({"data": data, "message":"Data received success"})
        except Exception as e:
            return jsonify({"message": str(e)})

    def post(self):
        try:
            data = request.form or request.get_json()
            print("data======", data)
            email = data.get("email")
            existing_email = User.query.filter_by(email=email).first()
            if existing_email:
                return jsonify({"message": "Email already exist."})

            new_user = User(first_name=data.get("first_name"),last_name=data.get("last_name"), email=data.get("email"),
                            password=data.get("password"), confirm_password=data.get("confirm_password"))
            mysql_db.session.add(new_user)
            mysql_db.session.commit()
            return jsonify({"Code": 201})
        except:
            return ""