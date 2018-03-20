from flask import Blueprint, render_template, request, make_response, jsonify
from functools import wraps
import os

from ..modules.index_module import ModuleClass
from ..modules.auth_module.models import User

template_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'templates')

static_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
static_dir = os.path.join(static_dir, 'static')

module = Blueprint('index',
    __name__,
    url_prefix='/index',
    static_folder=static_dir,
    template_folder=template_dir
)

def requires_login(api_method):
    @wraps(api_method)
    def verify_login(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {'status': 'fail', 'message': 'Bearer token malformed.'}
                return make_response(jsonify(responseObject)), 401
        elif 'auth_token' in request.cookies:
            try:
                auth_token = request.cookies.get('auth_token').split(" ")[1]
            except IndexError:
                responseObject = {'status': 'fail', 'message': 'Bearer token malformed.'}
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''

        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                if user:
                    return api_method(*args, **kwargs)
                else:
                    return render_template('login.html', title="Login",
                                    redirected="You need to login first, then try again")
        else:
            return render_template('login.html', title="Login",
                                   redirect_message="No auth token provided, please login")
    return verify_login


@module.route('/', methods=['GET', 'POST'])
@requires_login
def index():
    message = ModuleClass.default()
    return render_template('index.html', title="Index", message=message)