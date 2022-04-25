# Find 

## Find an action

```shell
find / -name "runlog-2021*.log" -printf '%h/%f\n'
```

```shell
find . -name "runlog.2021*.trace" -type f -exec gzip -f {} \;
```

## Search text in all files in a directory

```shell
grep -R "text" .
```
