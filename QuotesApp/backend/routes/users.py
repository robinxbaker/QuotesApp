from flask import Blueprint, request, jsonify
from models import db, User, Quote, SavedQuote
from flask_login import login_required, current_user

users = Blueprint('users', __name__)

# Get the current user's profile information
@users.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user_data = {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at,
        "quotes_count": len(current_user.quotes)
    }
    return jsonify(user_data), 200

# Get all quotes posted by the current user
@users.route('/my-quotes', methods=['GET'])
@login_required
def get_user_quotes():
    quotes = Quote.query.filter_by(user_id=current_user.id).all()
    result = [{"id": q.id, "content": q.content, "created_at": q.created_at} for q in quotes]
    return jsonify(result), 200

# Get all saved quotes by the user
@users.route('/saved', methods=['GET'])
@login_required
def get_saved_quotes():
    saved_quotes = SavedQuote.query.filter_by(user_id=current_user.id).all()
    result = [{"id": sq.quote.id, "content": sq.quote.content} for sq in saved_quotes]
    return jsonify(result), 200