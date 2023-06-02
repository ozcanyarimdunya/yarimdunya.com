# Find 

## Find an action

```shell
find / -name "runlog-2021*.log" -printf '%h/%f\n'
```

```shell
find . -name "runlog.2021*.trace" -type f -exec gzip -f {} \;
```

```shell
find /opt/data/detached -name ignored_* | xargs -exec rm -rf {}
```

## Search text in all files in a directory

```shell
grep -R "text" .
```
