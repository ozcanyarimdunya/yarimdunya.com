# Loops

## For loops

```shell
for i in {1..5} ; do
  echo "Number is $i"
done
```

```shell
for (( i = 0; i < 10; i++ )); do
  echo "Number is $i"
done
```

```shell
for i in $(ls /tmp/) ; do
  echo "File is $i"
done
```

## While loops

```shell
i=100
while [ $i -gt 10  ]; do
  echo "Number is $i"
  ((i--))
done
```

```shell
counter=0
while true; do
  if [ "${counter}" -gt 10 ]; then
      break 
  else
    echo "Counter is ${counter}"
    ((counter++))
    continue 
  fi
done
```

## Until loops

```shell
counter=10
until [ "${counter}" -lt 1 ]; do
  echo "Counter is ${counter}"
  ((counter--))
done
```

```shell
until [[ $(ping -c 1 blog.yarimdunya.com 2>/dev/null) ]]; do
  echo "Waiting for site to be up"
  sleep 1
done
```
