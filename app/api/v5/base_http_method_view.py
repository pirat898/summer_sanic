from sanic.views import HTTPMethodView


class BaseHTTPMethodView(HTTPMethodView):
    body_model = None
    url_model = None
    result_model = None
