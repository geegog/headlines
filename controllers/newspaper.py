from flask import Blueprint, request, json, jsonify

from headlines.models.newpaper import Company
from headlines.database import db_session
from sqlalchemy.exc import IntegrityError

save_company = Blueprint('save_company', __name__)
get_company = Blueprint('get_company', __name__)


@save_company.route('/new_company', methods=['POST'])
def add_company():
    j_data = json.loads(request.data)
    new_company = Company(**j_data)
    try:
        db_session.add(new_company)
        db_session.commit()
    except IntegrityError:
        return jsonify({
            'message': 'Newspaper company NOT created',
            'error': 'Record already exist!'
        })
    return jsonify({
            'message': 'Newspaper company created successful',
            'error': ''
        })


@get_company.route('/company', methods=['GET'])
def retrieve_company():
    company_id = request.args.get("id")
    company = Company.query.filter(Company.id == company_id).first()
    try:
        newspaper = company.serialize()
    except AttributeError:
        return jsonify({
            'message': 'Newspaper company with id: {id} does not exist'.format(id=company_id)
        })
    return jsonify(newspaper)
