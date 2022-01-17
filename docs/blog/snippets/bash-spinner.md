# Spinner in bash

```shell
function spinner() {
  timeout=${1:-10}; shift
  finish=$(($(date +%s) + ${timeout}))
  spin="/-\|"
  until [[ "$(date +%s)" -gt "${finish}" ]]; do
    idx=$(($(date +%s) % 4))
    echo -ne '\033[2K'
    echo -ne "\r${spin:$idx:1} ${@}"
  done
}

spinner 
spinner 5
spinner 15 "Continue"
```
