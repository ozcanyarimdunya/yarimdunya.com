# Inputs

## Read user input and assign to variable

```shell
read -p name "Enter  a name: "

echo "${name}"
```

```shell
#!/usr/bin/env bash

declare names=()

while true; do
  read -p "Enter name (q exit): " name
  if [[ "${name}" == "q" ]]; then
    break
  fi
  names+=("${name}")
done

for i in ${names[@]}; do
  echo "${i}"
done
```
