# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify, g, url_for
from flask_restful import reqparse, abort, Api, Resource, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from .common import printWellcome, bcolors, loadConfig, loadMode, resolveRelativeWorkingDirectory, \
    checkDefaultAdminSecret
import logging
import re


# initialization
app = Flask(__name__)

if loadMode() == True:  # If true debug  mode
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
else:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


config = loadConfig(logger)
try:
    app.config['SECRET_KEY'] = config["app"]["secretKey"]
    app.config['SQLALCHEMY_DATABASE_URI'] = resolveRelativeWorkingDirectory(config["app"]["databaseUri"])
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = config["app"]["commitOnTeardown"]
    tokenLife = config["tokenLife"]  # In seconds
    adminSecret = config["adminSecret"]
    checkDefaultAdminSecret(adminSecret)
    cors = config["CORS"]["enable"]
    origins = config["CORS"]["origins"]
    debug = config["debug"]
except KeyError:
    print(bcolors.WARNING+"Misformed config.json!"+bcolors.ENDC)
    exit()

# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
api = Api(app)
if cors:
    CORS(app, origins=origins)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=tokenLife):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route('/api/users', methods=['POST'])
def new_user():
    if pwd_context.verify(request.values.get('secret'), adminSecret) == False:
        abort(401)    # unauthorized
    username = request.values.get('username')
    password = request.values.get('password')
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(409)    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})


@app.route('/api/users/<int:id>')
@auth.login_required
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(tokenLife)
    return jsonify({'token': token.decode('ascii'), 'duration': tokenLife})

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})

def checkUser(vusers):
    # Check if it is a username or token auth
    user = User.verify_auth_token(auth.username())
    if user:
        return bool(user.username in vusers)
    else:
        return bool(auth.username() in vusers)

def getDomain(request):
    pattern_url_base = re.compile("(http|https):\/\/[a-zA-Z0-9_.]+:[0-9]*")
    return pattern_url_base.search(str(request)).group()

def getResourceURL(endpoint, selector_name = None, selector_value = None, absolute = False):
    if selector_name is None and selector_value is None:
        selector_name = "dummy_RDCH106"
        selector_value = "dummy_RDCH106"
    uri_field = {'url': fields.Url(endpoint)}
    selector = {selector_name: selector_value}
    if absolute:
        return getDomain(request) + marshal(selector, uri_field)["url"]
    else:
        return marshal(selector, uri_field)["url"]


def createDB():
    db_path = str(app.config['SQLALCHEMY_DATABASE_URI'].split('///')[1])
    if not os.path.exists(db_path):
        print(bcolors.WARNING + "Creating SQlite Database" + bcolors.ENDC)
        print(bcolors.OKBLUE + db_path + bcolors.ENDC)
        db.create_all()

def run():
    printWellcome()
    createDB()
    if config["SSL"]["activate"]:
        app.run(host=config["host"]["ip"], port=config["host"]["port"], debug=debug,
                processes=config["host"]["processes"], threaded=config["host"]["threaded"],
                ssl_context=(config["SSL"]["certificate"], config["SSL"]["key"]))
    else:
        app.run(host=config["host"]["ip"], port=config["host"]["port"], debug=debug,
                processes=config["host"]["processes"], threaded=config["host"]["threaded"])
