import webtest
import pytest

from safd import Application, text


def test_route_dispatch():
    app = Application()

    @app.route("/")
    def get(request, response):
        return "/"

    @app.route("/foo/baz")
    def post(request, response):
        return "/foo/baz"

    @app.route("/foo/(.*)")
    def get(request, response, id):
        return "/foo/id"

    @app.route("/foo/(.*)/baz")
    def insert(request, response, id):
        return "/foo/id/baz"

    
    f, params = app.dispatch("get", "/")
    assert params == [] and f(None, None) == "/"

    f, params = app.dispatch("post", "/foo/baz")
    assert params == [] and f(None, None) == "/foo/baz"

    f, params = app.dispatch("get", "/foo/1")
    assert params == ['1'] and f(None, None, *params) == "/foo/id"

    f, params = app.dispatch("insert", "/foo/1/baz")
    assert params == ['1'] and f(None, None, *params) == "/foo/id/baz"

def test_requset():
    app = Application()

    @app.route("/")
    @text
    def get(request, response):
        return "Hello World!"

    testapp = webtest.TestApp(app)

    resp = testapp.get('/')

    assert resp.text == "Hello World!"
