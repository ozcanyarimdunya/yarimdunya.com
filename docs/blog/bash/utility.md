# Utility

## loggers

```shell
success() {
  echo -e "\e[1;32m$1\e[0m"
}

info() {
  echo -e "\e[1;34m$1\e[0m"
}

warning() {
  echo -e "\e[1;33m$1\e[0m"
}

error() {
  echo -e "\e[1;31m$1\e[0m"
}

ask() {
  while true; do
    read -p "$(success "$1 (y/n) ?") " yn
    case $yn in
    [Yy]*) return 0 ;;
    [Nn]*) return 1 ;;
    *) error "Please answer y/Y or n/N" ;;
    esac
  done
}
```
