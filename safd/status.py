from functools import partial


class StatusCode:
    def __init__(self, code, text):
        self.__code = code
        self.__text = text

    def __str__(self):
        return f"{self.__code} {self.__text}"

    def __repr__(self):
        return f"{self.__code} {self.__text}"


status = StatusCode

OK = partial(status, 200, "OK")

CREATED = partial(status, 201, "CREATED")

ACCEPTED = partial(status, 202, "ACCEPTED")

NON_AUTHORITATIVE_INFORMATION = partial(status, 203, "NON AUTHORITATIVE INFORMATION")

NO_CONTENT = partial(status, 204, "NO CONTENT")

RESET_CONTENT = partial(status, 205, "RESET CONTENT")

PARTIAL_CONTENT = partial(status, 206, "PARTIAL CONTENT")

MULTI_STATUS = partial(status, 207, "MULTI STATUS")

MULTIPLE_CHOICES = partial(status, 300, "MULTIPLE CHOICES")

MOVED_PERMANENTLY = partial(status, 301, "MOVED PERMANENTLY")

MOVED_TEMPORARILY = partial(status, 302, "MOVED TEMPORARILY")

SEE_OTHER = partial(status, 303, "SEE OTHER")

NOT_MODIFIED = partial(status, 304, "NOT MODIFIED")

USE_PROXY = partial(status, 305, "USE PROXY")

TEMPORARY_REDIRECT = partial(status, 307, "TEMPORARY REDIRECT")

PERMANENT_REDIRECT = partial(status, 308, "PERMANENT REDIRECT")

BAD_REQUEST = partial(status, 400, 'BAD REQUEST')

UNAUTHORIZED = partial(status, 401, 'UNAUTHORIZED')

FORBIDDEN = partial(status, 403, 'FORBIDDEN')

NOT_FOUND = partial(status, 404, 'NOT fOUND')

METHOD_NOT_ALLOWED = partial(status, 405, 'METHOD NOT ALLOWED')

CONFLICT = partial(status, 409, 'CONFLICT')

GONE = partial(status, 410, 'GONE')

PRECONDITION_FAILED = partial(status, 412, 'PRECONDITION FAILED')

INTERNAL_SERVER_ERROR = partial(status, 500, 'INTERNAL SERVER ERROR')

BAD_GATEWAY = partial(status, 502, 'BAD GATEWAY')

