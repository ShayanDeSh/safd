import re
from safd.request import Request
from safd.response import Response

class Application:

    def __init__(self):
        self.request = None
        self.response = None
        self.routes = {}

    def __call__(self, environ, start_response):

        request = Request(environ)
        response = Response(start_response);

        verb = request.verb
        path = request.path

        f, p = self.dispatch(verb, path)
        response.body = f(request, response, *p)
        body = response.conclude()
        return body

            #body = self.handle_exception(e, start_response)
            #return body

    """
    I may add another way of routing using the tree I designed in my previous
    framework but this one which works with regex may work for now.
    """
    def route(self, pattern):
        def decorator(func):
            verb = func.__name__
            r = (re.compile(pattern), func)
            regs = self.routes.setdefault(verb, [])
            regs.append(r)
        return decorator

    def dispatch(self, verb, path):
        routes = self.routes
        patterns = routes.get(verb)
        if not patterns:
            """
            TODO: Raise appropriate exception
            """
            raise Exception
        for (pattern, func) in patterns:
            match = pattern.fullmatch(path)
            if not match:
                continue

            params = [p for p in match.groups()]
            return func, params

        """
        TODO: Raise appropriate exception
        """
        raise Exception


