# Run as user

```python
import os
import pwd
import subprocess


class LocalRunner:  # noqa
    @classmethod
    def run_as_user(cls, command, user, cwd):
        pwn = pwd.getpwnam(user)
        env = os.environ.copy()
        env.update(
            HOME=pwn.pw_dir,
            LOGNAME=pwn.pw_name,
            PWD=cwd,
            USER=pwn.pw_name,
        )
        process = subprocess.Popen(
            args=command,
            shell=True,
            preexec_fn=lambda: cls.pre_exec(pwn.pw_uid, pwn.pw_gid),
            cwd=cwd,
            env=env,
        )
        return_code = process.wait()
        out, err = process.communicate()
        return return_code, out, err

    @staticmethod
    def pre_exec(uid, gid):
        os.setgid(gid)
        os.setuid(uid)


code, out, err = LocalRunner.run_as_user(
    command="git push origin master",
    user="ozcanyarimdunya",
    cwd="/home/ozcanyarimdunya/repo/",
)
```
