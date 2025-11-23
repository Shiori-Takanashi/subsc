import pytest
from app import create_app
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig


def test_development_config():
    app = create_app(DevelopmentConfig)
    assert app.config['DEBUG'] is True
    assert app.config['TESTING'] is False


def test_production_config():
    app = create_app(ProductionConfig)
    assert app.config['DEBUG'] is False
    assert app.config['TESTING'] is False


def test_testing_config():
    app = create_app(TestingConfig)
    assert app.config['TESTING'] is True
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'
