import wsgiref.util as wsgiutil
from urllib.parse import parse_qs
from safd.helpers import Lazy


class Request:
    def __init__(self, environ):
        self.environ = environ

    @Lazy
    def verb(self):
        return self.environ['REQUEST_METHOD'].lower()

    @Lazy
    def query(self):
        if 'QUERY_STRING' not in self.environ:
            return {}
        return { 
            k: v[0] if len(v) == 1 else v for k, v in parse_qs(
            self.environ['QUERY_STRING'],
            keep_blank_values=True,
            strict_parsing=False).items()
        }

    @Lazy
    def path(self):
        return self.environ['PATH_INFO'].lower()

    @Lazy
    def URI(self):
        return wsgiutil.request_uri(self.environ, include_query=True)

    @Lazy
    def content_type(self):
        content_type = self.environ.get("CONTENT_TYPE")
        if content_type:
            return content_type.split(';')[0]
        return None

    @Lazy
    def content_length(self):
        length = self.environ.get("CONTENT_LENGTH")
        return None if not v or not v.strip() else int(v)

    @Lazy
    def cookies(self):
        cookie = SimpleCookie()
        if 'HTTP_COOKIE' in self.environ:
            cookie.load(self.environ['HTTP_COOKIE'])
        return cookie


