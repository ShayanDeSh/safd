#Simple As Fuck Dispatcher

```
from safd import Application, json, code
from safd.status import BAD_REQUEST

app = Application()

@app.route("/")
@code(BAD_REQUEST)
@json
def get(request, response):
    return "Simplicty is the key to maintainability"
```
