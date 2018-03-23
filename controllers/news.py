from flask import Blueprint, request, json, jsonify

from headlines.models.news import News
from headlines.database import db_session
from sqlalchemy.exc import IntegrityError

save_news = Blueprint('save_news', __name__)
get_all_news = Blueprint('get_all_news', __name__)
get_news_by_category = Blueprint('get_news_by_category', __name__)


@save_news.route('/add_news', methods=['POST'])
def add_news():
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


@get_all_news.route('/news', methods=['GET'])
def all_news():
    news = News.query.all()
    return jsonify(news=[n.serialize() for n in news])


@get_news_by_category.route('/news_by_category', methods=['GET'])
def news_by_category():
    category_id = request.args.get("id")
    news = News.query.filter(News.id == category_id)
    return jsonify(news=[n.serialize() for n in news])

