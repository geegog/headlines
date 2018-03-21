from flask import Blueprint, request, json, jsonify

from headlines.models.categories import Category
from headlines.database import db_session
from sqlalchemy.exc import IntegrityError

save_category = Blueprint('save_category', __name__)
get_all_categories = Blueprint('get_all_categories', __name__)


@save_category.route('/new_category', methods=['POST'])
def add_company():
    j_data = json.loads(request.data)
    new_category = Category(**j_data)
    try:
        db_session.add(new_category)
        db_session.commit()
    except IntegrityError:
        return jsonify({
            'message': 'Category NOT created',
            'error': 'Category already exist!'
        })
    return jsonify({
            'message': 'Category created successful',
            'error': ''
        })


@get_all_categories.route('/categories', methods=['GET'])
def retrieve_company():
    categories = Category.query.all()
    return jsonify(category=[c.serialize() for c in categories])
