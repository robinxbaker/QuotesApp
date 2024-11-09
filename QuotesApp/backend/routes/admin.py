from flask import Blueprint, request, jsonify
from models import db, Quote, User, Flag
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)

# Check if the user is an admin
def is_admin(user):
    return user.is_admin

# List all flagged quotes for review
@admin.route('/flagged', methods=['GET'])
@login_required
def get_flagged_quotes():
    if not is_admin(current_user):
        return jsonify({"error": "Access denied"}), 403

    flagged_quotes = Flag.query.all()
    result = [{
        "quote_id": flag.quote_id,
        "reason": flag.reason,
        "user_id": flag.user_id,
        "created_at": flag.created_at
    } for flag in flagged_quotes]
    
    return jsonify(result), 200

# Admin can delete a flagged quote
@admin.route('/delete_quote/<int:quote_id>', methods=['DELETE'])
@login_required
def delete_flagged_quote(quote_id):
    if not is_admin(current_user):
        return jsonify({"error": "Access denied"}), 403

    quote = Quote.query.filter_by(id=quote_id).first()
    if quote:
        db.session.delete(quote)
        db.session.commit()
        return jsonify({"message": "Quote deleted successfully"}), 200
    return jsonify({"error": "Quote not found"}), 404