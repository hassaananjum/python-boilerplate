from flask import request, make_response, jsonify, redirect, url_for, Response
from flask.views import MethodView

from .models import User
from ... import bcrypt

class LoginAPI(MethodView):
    """
    User Login Resource
    """
    def post(self):
        # get the post data
        redirect_to_index = False
        try:
            post_data = request.get_json()
            if not post_data:
                post_data = {'email': request.form['email'], 'password':
                    request.form['password']}
                redirect_to_index = True
        except Exception:
            post_data = {'email': request.form['email'], 'password': request.form['password']}
            redirect_to_index = True
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user and bcrypt.check_password_hash(
                user.password, post_data.get('password')
            ):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    if redirect_to_index:
                        resp = redirect(url_for('index.index'))
                        resp.is_redirect = True
                        resp.set_cookie('auth_token', 'Bearer ' + auth_token.decode(), httponly=True)
                        return resp
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    resp = make_response(jsonify(responseObject))
                    resp.set_cookie('auth_token', 'Bearer ' + auth_token.decode(),
                                    httponly=True)
                    return resp
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500

login_view = LoginAPI.as_view('login_api')