from flask import Blueprint

from ..modules.auth_module import RegisterAPI, LoginAPI, UserAPI, LogoutAPI

auth_blueprint = Blueprint('auth', __name__)

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=RegisterAPI.registration_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=LoginAPI.login_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=UserAPI.user_view,
    methods=['GET']
)

auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=LogoutAPI.logout_view,
    methods=['POST']
)