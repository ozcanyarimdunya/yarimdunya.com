# Custom dict config

```python
import json
import re


class Config(dict):
    re_pattern = re.compile(r"^(\w+)\s*=(.*)$")

    @classmethod
    def from_env(cls, f):
        items = {}
        with open(f, mode="r") as fp:
            for each in fp.read().splitlines():
                match = re.match(cls.re_pattern, each.strip())
                if not match:
                    continue
                items[match.group(1)] = match.group(2).strip()
        return cls(**items)

    @classmethod
    def from_string(cls, string):
        items = {}
        for each in string.split():
            match = re.match(cls.re_pattern, each.strip())
            if not match:
                continue
            items[match.group(1)] = match.group(2).strip()
        return cls(**items)

    @classmethod
    def from_json(cls, f):
        with open(f, mode="r") as fp:
            items = json.load(fp, encoding="utf-8")
        return cls(**items)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        return self[item]

```

**Usage**

```python
cfg = Config.from_json("env.json")
cfg = Config.from_env("env.env")
cfg = Config.from_string(text)
```
