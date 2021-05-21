from functools import wraps

class Lazy:
    __slots__ = ('f',)

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, t=None):
        f = self.f
        if obj is None:
            return f
        val = f(obj)
        setattr(obj, f.__name__, val)
        return val

def statuscode(code):
    def decorator(handler):
        def wrapper(request, response, *a, **k):
            result = handler(request, response, *a, **k)
            response.status = code if isinstance(code, str) else \
                code().status
            return result
        return wrapper
    return decorator

def json(handler):
    @wraps(handler)
    def wrapper(request, response, *args):
        response.content_type = 'application/json'
        response.charset = 'utf-8'
        body = handler(request, response, *args)
        body = ujson.dumps(body)
        return body
    return wrapper

def html(handler):
    @wraps(handler)
    def wrapper(request, response, *args):
        response.content_type = 'text/html'
        response.charset = 'utf-8'
        body = handler(request, response, *args)
        return body
    return wrapper

def text(handler):
    @wraps(handler)
    def wrapper(request, response, *args):
        response.content_type = 'text/plain'
        response.charset = 'utf-8'
        body = handler(request, response, *args)
        return body
    return wrapper

