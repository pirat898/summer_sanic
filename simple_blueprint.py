from sanic.response import json
from sanic import Sanic, Blueprint


bp1 = Blueprint('bp1', url_prefix='/v1')
bp2 = Blueprint('bp2', url_prefix='/v2')

bp = Blueprint.group(bp1, bp2, url_prefix='/api')


@bp1.route('/test')
async def bp_root_1(request):
    return json({'my': 'blueprint 1'})


@bp2.route('/test')
async def bp_root_2(request):
    return json({'my': 'blueprint 2'})


async def before_server_start(app, loop):
    print(f"Before server start")


async def before_server_stop(app, loop):
    print(f"Before server stop")


async def simple(request):
    url = request.app.url_for('bp1.ololololo')
    return json({'url': url})


if __name__ == "__main__":

    web_app = Sanic()

    web_app.listener('before_server_start')(before_server_start)
    web_app.listener('before_server_stop')(before_server_stop)

    web_app.blueprint(bp)

    web_app.add_route(simple, '/simple')

    web_app.run(host="0.0.0.0", port=8080, debug=True)
