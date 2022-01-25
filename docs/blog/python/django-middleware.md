# Middleware in Django


Create a python file named as middlewares.py under project root and write your middleware as below

```python

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

```

Add your middleware class to **settings.py**

```python
MIDDLEWARE = [
    ... # Your previous middlewares
    'project_root.middlewares.SimpleMiddleware',
]
```
