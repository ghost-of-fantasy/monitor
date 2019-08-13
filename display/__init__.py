import os

from flask import Flask
from display.settings import config
from display.extensions import toolbar, bootstrap, db, moment, ckeditor, mail
from display.commands import register_commands
from display.blueprints.article import article_bp


# 使用工厂函数创建程序实例使得测试和部署更加方便，不必将加载的配置写死在某处
def create_app(config_name=None):
    """
    创建app的函数
    :param config_name:
    :return:
    """
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('display')
    app.config.from_object(config[config_name])
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    register_extensions(app)  # 注册扩展
    register_blueprints(app)  # 注册蓝本
    register_commands(app)  # 注册自定义命令行

    return app


def register_extensions(app):
    """
    注册扩展
    :param app:
    :return:
    """
    toolbar.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)


def register_blueprints(app):
    """
    注册蓝本
    :param app:
    :return:
    """
    app.register_blueprint(article_bp, url_prefix='/')