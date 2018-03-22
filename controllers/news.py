from flask import Blueprint, request, json, jsonify

from headlines.models.news import News
from headlines.database import db_session
from sqlalchemy.exc import IntegrityError

save_news = Blueprint('save_news', __name__)
get_all_news = Blueprint('get_all_news', __name__)


@save_news.route('/add_news', methods=['POST'])
def add_company():
    j_data = json.loads(request.data)
    new_news = News(**j_data)
    try:
        db_session.add(new_news)
        db_session.commit()
    except IntegrityError:
        return jsonify({
            'message': 'News NOT created',
            'error': 'News already exist!'
        })
    return jsonify({
            'message': 'News created successful',
            'error': ''
        })
