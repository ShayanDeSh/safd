import re

class Router:
    def __init__():
        self.routes = {}

    def __call__(self, environ, start_response):
        pass


    def route(self, pattern):
        def decorator(func):
            verb = func.__name__
            r = (re.compile(regex), func)
            regs = self.routes.setdefault(verb, [])
            regs.append(r)
        return decorator

