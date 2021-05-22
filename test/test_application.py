import webtest
import pytest

from safd import Application, text, json, html, code
from safd.status import BAD_REQUEST


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

def test_text_response():
    app = Application()

    @app.route("/")
    @text
    def get(request, response):
        return "Hello World!"

    testapp = webtest.TestApp(app)
    resp = testapp.get('/')

    assert resp.text == "Hello World!" and resp.content_type == "text/plain"

def test_json_response():
    app = Application()

    @app.route("/")
    @json
    def get(request, response):
        return {"foo": "baz"}

    testapp = webtest.TestApp(app)
    resp = testapp.get('/')

    assert resp.content_type == "application/json" and resp.json == {"foo": "baz"}

def test_html_response():
    app = Application()

    @app.route("/")
    @html
    def get(request, response):
        return "<html></html>"

    testapp = webtest.TestApp(app)
    resp = testapp.get('/')
    resp_html = resp.html
    assert resp.content_type == "text/html" and resp.html == resp_html


def test_status_code():
    app = Application()

    @app.route("/")
    @code(BAD_REQUEST)
    @text
    def get(request, response):
        return "Testing status code"

    testapp = webtest.TestApp(app)
    resp = testapp.get('/', status="*")

    assert resp.status == "400 BAD REQUEST"

