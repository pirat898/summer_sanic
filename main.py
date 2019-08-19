from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound, InvalidUsage
from schematics.exceptions import BaseError
from sanic_transmute import add_swagger

from app.api.blueprint_group import api_blueprint_group


def sanic_error_handler(status):
    async def custom_error_handler(request, exception):
        return json({'success': False, 'error': str(exception)}, status=status)
    return custom_error_handler


web_app = Sanic()

web_app.blueprint(api_blueprint_group)
web_app.error_handler.add(BaseError, sanic_error_handler(400))
web_app.error_handler.add(NotFound, sanic_error_handler(404))
web_app.error_handler.add(InvalidUsage, sanic_error_handler(400))
web_app.error_handler.add(Exception, sanic_error_handler(500))


add_swagger(web_app, "/swagger.json", "swagger")


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=8080, debug=True, auto_reload=False)
