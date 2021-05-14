import pytest
from safd import Router


def test_route_dispatch():
    app = Router()

    @app.route("/")
    def get():
        return "/"

    @app.route("/foo/baz")
    def post():
        return "/foo/baz"

    @app.route("/foo/(.*)")
    def get(id):
        return "/foo/id"

    @app.route("/foo/(.*)/baz")
    def insert(id):
        return "/foo/id/baz"

    
    f, params = app.dispatch("get", "/")
    assert params == [] and f() == "/"

    f, params = app.dispatch("post", "/foo/baz")
    assert params == [] and f() == "/foo/baz"

    f, params = app.dispatch("get", "/foo/1")
    assert params == ['1'] and f(*params) == "/foo/id"

    f, params = app.dispatch("insert", "/foo/1/baz")
    assert params == ['1'] and f(*params) == "/foo/id/baz"


