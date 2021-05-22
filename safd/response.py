from wsgiref.headers import Headers
from http.cookies import SimpleCookie
from datetime import datetime, timedelta

class Response(Headers):
    def __init__(self, start_response):
        super().__init__()
        self.charset = "utf-8"
        self.__cookies = SimpleCookie()
        self.is_chunked = False
        self.start_response = start_response
        self.status = "200 OK"

    @property
    def charset(self):
        return self._charset

    @charset.setter
    def charset(self, val):
        self._charset = val

    @property
    def content_type(self):
        content_type = self.get('Content-Type')
        if content_type:
            return content_type.split(';')[0]
        return None

    @content_type.setter
    def content_type(self, v):
        if v is None:
            del self['Content-Type']
        else:
            self['Content-Type'] = '%s; charset=%s' % (v, self.charset)

    def cookie(self, name, value, options={}, path='/'):
        options['path'] = path
        self.__cookies[name] = value
        if options:
            for k, v in options.items():
                self.__cookies[name][k] = v
        return self

    def remove_cookie(self, name, path='/'):
        self.__cookies[name] = ""
        self.__cookies[name]['path'] = path
        print(datetime.utcnow())
        expires = datetime.utcnow()
        expires = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        self.__cookies[name]['Expires'] = expires

    def conclude(self):
        body = self.body
        if body is None:
            self.body = []

        elif isinstance(body, (str, bytes)):
            body = [body]

        if self.charset:
            body = [i.encode(self.charset) for i in body]

        self['content-length'] = str(sum(len(i) for i in body))

        cookie = self.__cookies.output()
        if cookie:
            for line in cookie.split('\r\n'):
                self.add_header(*line.split(': '))
        self.start_response(self.status, self.items())

        return body

