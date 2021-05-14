import re

class Router:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        pass

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
