from flask import Blueprint, redirect, request, url_for, session, jsonify
from utils.oauth import get_google_login_uri, client, get_google_provider_cfg
from models import db, User
from flask_login import login_user, logout_user
import requests
import json

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return redirect(get_google_login_uri())

@auth.route('/callback')
def callback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(token_url, headers=headers, data=body, auth=(client.client_id, client.client_secret))
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    user_info = userinfo_response.json()

    # Check if user exists or create a new one
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(username=user_info['name'], email=user_info['email'], google_id=user_info['sub'])
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return jsonify({"message": "Logged in successfully"})

@auth.route('/logout')
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})