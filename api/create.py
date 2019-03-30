from flask import Flask

from api.blueprints.testbp import testbp


def create_app(*config):
    '''
    可通过config来创建不同的app实例
    '''
    app=Flask(__name__)
    app.config.from_object('api.config.setting')
    app.register_blueprint(testbp)
    return app
