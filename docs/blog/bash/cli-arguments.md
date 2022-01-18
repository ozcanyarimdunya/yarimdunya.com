# Argparse in bash

```shell
#!/usr/bin/env bash

options=$(getopt -l "servers:,file:,help,verbose" -o ":s:fhv" --name "$0" -- "$@")

VERBOSE=false
SERVERS=()
while true; do
  case $1 in
  -h|--help)
    echo "help"
    exit
    ;;
  -v|--verbose)
    VERBOSE=true
    ;;
  -s|--servers)
    shift
    SERVERS+=("$1")
    ;;
  -f|--file)
    shift
    FILE="$1"
    ;;
  *)
    shift
    break
    ;;
  esac
  shift
done

if ${VERBOSE}; then
  echo "Verbose"
else
  echo "Not verbose"
fi

for s in ${SERVERS[@]}; do
  echo "Server: ${s}"
done

echo "File is ${FILE}"

```

**Usage**

```shell
$ ./file.sh -v -s s1 --servers s2 -f /opt/test.txt
```

**Output**

```shell
Verbose
Server: s1
Server: s2
File is /opt/test.txt
```
