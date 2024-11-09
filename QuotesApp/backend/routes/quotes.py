from flask import Blueprint, request, jsonify
from models import db, Quote, User
from flask_login import login_required, current_user

quotes = Blueprint('quotes', __name__)

@quotes.route('/quotes', methods=['POST'])
@login_required
def create_quote():
    data = request.json
    content = data.get('content')
    tags = data.get('tags', '')
    is_public = data.get('is_public', True)
    is_anonymous = data.get('is_anonymous', False)

    if not content:
        return jsonify({"error": "Content is required"}), 400

    new_quote = Quote(
        user_id=current_user.id,
        content=content,
        tags=tags,
        is_public=is_public,
        is_anonymous=is_anonymous
    )
    db.session.add(new_quote)
    db.session.commit()
    return jsonify({"message": "Quote created successfully"}), 201

@quotes.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = Quote.query.filter_by(is_public=True).all()
    result = [{"id": q.id, "content": q.content, "tags": q.tags, "created_at": q.created_at} for q in quotes]
    return jsonify(result), 200

@quotes.route('/quotes/<int:quote_id>', methods=['DELETE'])
@login_required
def delete_quote(quote_id):
    quote = Quote.query.filter_by(id=quote_id, user_id=current_user.id).first()
    if not quote:
        return jsonify({"error": "Quote not found or not authorized"}), 404

    db.session.delete(quote)
    db.session.commit()
    return jsonify({"message": "Quote deleted successfully"}), 200