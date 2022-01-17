# Conditions

## Single line

```shell
[[ "x" == "x" ]] && echo "Ok!"
```

## Multi line

```shell
counter=0
if [[ "${counter}" == 0 ]]; then
  echo "0"
fi
```

```shell
zone=$(hostname) # my-pc-01
if [[ "${zone}" == my* ]]; then
  echo "${zone} startswith my*"
else
  echo "${zone} doesn't start with my*"
fi
```
