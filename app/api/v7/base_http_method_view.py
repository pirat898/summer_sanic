import typing
from sanic.views import HTTPMethodView
from sanic.response import json
from schematics.exceptions import BaseError
from sanic.exceptions import InvalidUsage


class BaseHTTPMethodView(HTTPMethodView):
    body_model = None
    body_params = None
    url_model = None
    url_params = None
    result_model = None
    status_code = 200

    async def dispatch_request(self, request, *args, **kwargs):
        self.load_input(request)
        handler_coroutine = super().dispatch_request(request, *args, **kwargs)
        result = await handler_coroutine
        return self.serialize_result(result)

    def load_input(self, request):
        if self.url_model:
            try:
                url_model = self.url_model(request.args)
                url_model.validate()
            except BaseError as ex:
                raise InvalidUsage(f'Error in data: {ex.to_primitive()}')
            self.url_params = url_model.to_native()

        if self.body_model:
            try:
                body_model = self.body_model(request.json, strict=True)
                body_model.validate()
            except BaseError as ex:
                raise InvalidUsage(f'Error in data: {ex.to_primitive()}')
            self.body_params = body_model.to_native()

    def serialize_result(self, result):
        if self.result_model:
            if isinstance(result, typing.Mapping):
                result = self.result_model(result, strict=False).to_primitive()

            elif isinstance(result, typing.Iterable):
                result = [self.result_model(x, strict=False).to_primitive() for x in result]

        return json(result, status=self.status_code)
