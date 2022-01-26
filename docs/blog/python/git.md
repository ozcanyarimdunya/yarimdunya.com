# Git with Python

Run git commands from python

```python
import os
import shlex
import subprocess


def run(command):
    os.chdir("/path/to/repo/")
    process = subprocess.Popen(
        shlex.split(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = process.communicate()
    out, err = out.decode("utf-8"), err.decode("utf-8")
    assert not err, err
    return out


run("git status -s")
run('git commit -m "Add xyz"')
run("git push https://{TOKEN}@github.com/username/repo.git")
```

