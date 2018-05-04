from flask import Blueprint, Response

from kata_api_entreprise.service import api_entreprise_service

bp = Blueprint('myapp', __name__)


@bp.route('/entreprise/<siret>')
def index(siret):
    if int(siret) < 10000000000000 or int(siret) > 99999999999999:
        return Response(status=404)
    my_request = api_entreprise_service.request_wrapper(siret)
    my_response = Response(my_request.text, mimetype=my_request.headers['Content-Type'])
    return my_response
