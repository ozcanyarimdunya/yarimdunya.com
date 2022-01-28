# Class documentation

```python
class User:
    """A User class

    Args:
        name: Name of user

    Keyword Args:
        age: Age of user

    Attributes:
        name: Attr name
        age: Attr age

    Raises:
        ValueError: If no user provided

    Warnings:
        DeprecatedWarnings: If age provided

    Methods:
        say: Simple message

    Examples: https://yarimdunya.com/examples

    See Also: https://yarimdunya.com

    Notes: You shall not pass!

    >>> user = User("name", 30)
    >>> user.say()
    "Hello, name. You're 30 years old."
    """

    def __init__(self, name, age=28):
        self.name = name
        self.age = age

    def say(self):
        """Say Hello

        Returns: Greeting message

        """
        return f"Hello, {self.name}. You're {self.age} years old."

```