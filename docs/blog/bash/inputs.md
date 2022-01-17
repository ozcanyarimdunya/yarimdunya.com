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

## Press any key to continue ...

```shell
while read -r -n 1 key; do
  if [ "$key" == "y" ]; then
    echo "Break .."
    break
  fi
  echo "Continue"
done
```
