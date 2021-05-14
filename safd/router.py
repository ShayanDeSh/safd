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

    def dispatch(self, verb, path):
        routes = self.routes
        patterns = routes.get(verb)
        if not patterns:
            """
            TODO: Raise appropriate exception
            """
            raise Exception
        for (pattern, func) in patterns:
            match = pattern.match(path)
            if not match:
                continue

            params = [p for p in match.groups()]
            return f, params

        """
        TODO: Raise appropriate exception
        """
        raise Exception
