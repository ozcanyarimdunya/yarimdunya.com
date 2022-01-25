# Flask | Class Based Views

Sample class based views in flask

## URL schema

| url      | method     | description          |
|----------|------------|----------------------|
| `/`      | **GET**    | Get list of users    |
| `/`      | **POST**   | Create new user      |
| `/<id>/` | **GET**    | Get an user by id    | 
| `/<id>/` | **PUT**    | Update an user by id | 
| `/<id>/` | **DELETE** | Delete an user by id | 

## app.py

```python
from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)})


class UserAPI(MethodView):
    users = [
        {"pk": 1, "username": "Bret"},
        {"pk": 2, "username": "Antonette"},
        {"pk": 3, "username": "Samantha"},
        {"pk": 4, "username": "Karianne"},
        {"pk": 5, "username": "Kamren"},
    ]

    def get_user(self, pk):
        user = next(filter(lambda it: it['pk'] == pk, self.users), None)
        assert user is not None, "User not found"
        return user

    def get(self, pk=None):
        if pk is None:
            return jsonify(self.users)

        user = self.get_user(pk)
        return jsonify(user)

    def post(self):
        json = request.get_json()
        pk = json['pk']
        username = json['username']
        self.users.append({'pk': pk, 'username': username})
        return jsonify(self.users)

    def put(self, pk):
        json = request.get_json()
        username = json['username']
        user = self.get_user(pk)
        self.users.remove(user)
        self.users.append({'pk': pk, 'username': username})
        return jsonify(self.users)

    def delete(self, pk):
        user = self.get_user(pk)
        self.users.remove(user)
        return jsonify(self.users)


view = UserAPI.as_view('users')
app.add_url_rule(
    rule='/', 
    view_func=view, 
    methods=['GET', 'POST'],
)
app.add_url_rule(
    rule='/<int:pk>/', 
    view_func=view, 
    methods=['GET', 'PUT', 'DELETE'],
)

if __name__ == '__main__':
    app.run()
```

## Usage

```shell
python app.py
```
