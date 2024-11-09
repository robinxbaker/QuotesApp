from flask import url_for, redirect, request
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
import os

client = WebApplicationClient(os.getenv("GOOGLE_CLIENT_ID"))

def get_google_provider_cfg():
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()

def get_google_login_uri():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=url_for("auth.callback", _external=True),
        scope=["openid", "email", "profile"],
    )
    return request_uri