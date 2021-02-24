from flask import Flask
from api import __version__ as _version
my_app = Flask(__name__)

@my_app.route('/health')
def health():
    return 'Health: Ok!'

@my_app.route('/')
def get_data():
    # reg_version = get_version()
    # return {
    #     "reg_version": reg_version,
    #     "api_version": _version
    # }
    return { "api_version": _version }

@my_app.route('/new')
def write_and_get_data():
    # reg_version = get_version()
    # return {
    #     "reg_version": reg_version,
    #     "api_version": _version
    # }
    return { "api_version": _version }