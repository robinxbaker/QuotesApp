from flask import Blueprint, request, jsonify
from models import db, Rating, Quote
from flask_login import login_required, current_user

ratings = Blueprint('ratings', __name__)

# Add or update a rating for a quote
@ratings.route('/rate/<int:quote_id>', methods=['POST'])
@login_required
def rate_quote(quote_id):
    data = request.json
    rating_value = data.get('rating')

    if not (1 <= rating_value <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    rating = Rating.query.filter_by(user_id=current_user.id, quote_id=quote_id).first()
    if rating:
        rating.rating = rating_value
        rating.updated_at = datetime.utcnow()
    else:
        rating = Rating(user_id=current_user.id, quote_id=quote_id, rating=rating_value)
        db.session.add(rating)

    db.session.commit()
    return jsonify({"message": "Rating submitted"}), 200

# Get all ratings for a specific quote
@ratings.route('/ratings/<int:quote_id>', methods=['GET'])
def get_quote_ratings(quote_id):
    ratings = Rating.query.filter_by(quote_id=quote_id).all()
    result = [{"user_id": r.user_id, "rating": r.rating, "updated_at": r.updated_at} for r in ratings]
    return jsonify(result), 200