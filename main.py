from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound, InvalidUsage
# from sanic_openapi import swagger_blueprint, doc
from sanic_transmute import add_swagger, add_route

from app.api.blueprint_group import api_blueprint_group


def sanic_error_handler(status):
    async def custom_error_handler(request, exception):
        return json({'success': False, 'error': str(exception)}, status=status)
    return custom_error_handler


web_app = Sanic()

web_app.blueprint(api_blueprint_group)
# web_app.error_handler.add(NotFound, sanic_error_handler(404))
# web_app.error_handler.add(InvalidUsage, sanic_error_handler(400))
# web_app.error_handler.add(Exception, sanic_error_handler(500))


# web_app.blueprint(swagger_blueprint)
# web_app.config.API_VERSION = '1.0.0'
# web_app.config.API_TITLE = 'Summer Sanic'
# web_app.config.API_DESCRIPTION = 'Summer Sanic'
# web_app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']


add_swagger(web_app, "/swagger.json", "swagger")


# doc.route_specs[1].description = 'olololo'
# print(f"doc.route_specs: {doc.route_specs}")

# SWAGGER_ATTR_NAME = "_tranmute_swagger"
#
# if not hasattr(web_app, SWAGGER_ATTR_NAME):
#     setattr(web_app, SWAGGER_ATTR_NAME, SwaggerSpec())
#
# app._tranmute_swagger.add_path('/ttt/users', )

if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=8080, debug=True, auto_reload=False)
