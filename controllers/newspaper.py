from flask import Blueprint, request

save_company = Blueprint('save_company',  __name__)
get_company = Blueprint('get_company',  __name__)


@save_company.route('/new_company', methods=['POST'])
def save_company(company):
    return ""


@get_company.route('/get_company', methods=['GET'])
def save_company():
    company_id = request.args.get("id")
    return ""
