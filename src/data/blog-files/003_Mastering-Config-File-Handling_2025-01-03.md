## Mastering Configuration File Handling in Python: A Comprehensive Guide

Handling configuration files efficiently is a critical part of any software project. Configurations allow us to keep
application settings flexible and manageable. In this blog post, we’ll explore a Python class designed to simplify
working with various configuration file formats, including JSON, YAML, and `.env` files.

### The Code: A Unified Config Loader

Below is a Python class, `Config`, which abstracts the loading of configuration files. The class supports `.json`,
`.yaml`/`.yml`, and `.conf`/`.env` file formats, making it a versatile tool for developers.

```python
import json
import re
from pathlib import Path

import yaml


class Config(dict):
    def __init__(self, file_or_config: (str, Path, dict)):
        if isinstance(file_or_config, dict):
            super().__init__(file_or_config)
            return
        file = file_or_config if isinstance(file_or_config, Path) else Path(file_or_config)
        assert file.is_file(), f"File {file} does not exist"
        self.load(file)
        super().__init__()

    def load(self, file: Path):
        if file.suffix == ".json":
            self._load_json(file)
        elif file.suffix in [".conf", ".env"]:
            self._load_conf(file)
        elif file.suffix in [".yaml", ".yml"]:
            self._load_yaml(file)
        else:
            raise ValueError(f"Unsupported file type: {file.suffix}")

    def _load_json(self, file: Path):
        with file.open(mode="r") as fp:
            self.update(json.load(fp))

    def _load_conf(self, file: Path):
        pattern = re.compile(r'^(\w+)\s*=\s*"?([^"]*|\w[^"])"?$')
        with file.open(mode="r") as fp:
            for line in fp:
                match = pattern.match(line)
                if not match:
                    continue
                key, value = match.groups()
                self[key] = value.strip()

    def _load_yaml(self, file: Path):
        with file.open(mode="r") as fp:
            self.update(yaml.safe_load(fp))


def main():
    config1 = Config({"name": "test"})
    print(config1)

    config2 = Config("/opt/config.json")
    print(config2)

    config3 = Config("/opt/config.conf")
    print(config3)

    config4 = Config("/opt/config.yaml")
    print(config4)


if __name__ == "__main__":
    main()
```

---

### Breaking It Down

#### 1. **Class Overview**

The `Config` class inherits from Python’s `dict`, allowing it to act as a dictionary. This provides seamless access to
configuration values using dictionary-style syntax.

```python
config = Config("/path/to/config.json")
print(config["some_key"])
```

#### 2. **Supported Formats**

- **JSON**: Parsed using Python’s built-in `json` module.
- **YAML**: Requires the `PyYAML` library (`pip install pyyaml`).
- **Conf/Env Files**: Parsed with a custom regex pattern to extract key-value pairs.

#### 3. **Initialization**

The class accepts a file path or a dictionary as input:

- **File Input**: The `load` method is invoked to parse the file based on its extension.
- **Dictionary Input**: The input is directly loaded into the class instance.

#### 4. **File Loaders**

- **JSON**:
  ```python
  def _load_json(self, file: Path):
      with file.open(mode="r") as fp:
          self.update(json.load(fp))
  ```
- **Conf/Env**:
  ```python
  def _load_conf(self, file: Path):
      pattern = re.compile(r'^(\w+)\s*=\s*"?([^"]*|\w[^"])"?$')
      with file.open(mode="r") as fp:
          for line in fp:
              match = pattern.match(line)
              if not match:
                  continue
              key, value = match.groups()
              self[key] = value.strip()
  ```
- **YAML**:
  ```python
  def _load_yaml(self, file: Path):
      with file.open(mode="r") as fp:
          self.update(yaml.safe_load(fp))
  ```

---

### Key Features

- **Ease of Use**: Load a configuration file in just one line of code.
- **Format-Agnostic**: Switch between JSON, YAML, and `.conf`/`.env` without changing your implementation.
- **Error Handling**: Ensures unsupported file formats are caught with meaningful error messages.

---

### Example Usage

1. **Loading a JSON File**
   ```python
   config = Config("/path/to/config.json")
   print(config["api_key"])
   ```

2. **Loading a YAML File**
   ```python
   config = Config("/path/to/config.yaml")
   print(config["database"]["host"])
   ```

3. **Loading an `.env` File**
   ```python
   config = Config("/path/to/.env")
   print(config["SECRET_KEY"])
   ```

4. **Using a Predefined Dictionary**
   ```python
   config = Config({"debug": True, "timeout": 30})
   print(config["debug"])
   ```

---

### Why Use This Class?

- **Unified Interface**: No need to write separate parsers for each configuration format.
- **Scalability**: Easily extendable to support more file types if needed.
- **Maintainability**: Keeps configuration-related logic centralized and reusable.

---

### Conclusion

The `Config` class is a robust and flexible solution for managing configuration files in Python projects. By
consolidating multiple file formats into a single interface, it simplifies the development process and reduces
boilerplate code.

Feel free to clone, adapt, or integrate this utility into your projects.

Happy coding! 🚀
