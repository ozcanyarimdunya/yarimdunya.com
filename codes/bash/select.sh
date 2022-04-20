#!/usr/bin/env bash

function print() {
  echo -e "\e[1;34m${*}\e[0m"
}

function prompt() {
  while true; do
    read -r -p "→ $1 [y/N] " answer
    case ${answer} in
      [Yy]*) return 0 ;;
      [Nn]*) return 1 ;;
      *) print_error "Please answer y/Y or n/N" ;;
    esac
  done
}

function main() {
  PS3="Select a mode: "
  select choice in apply rollback; do
    case ${choice} in
      apply)
        print "Running function _apply"
        break
        ;;
      rollback)
        if prompt "Are your sure? "; then
          print "Running function _rollback"
          break
        fi
        ;;
      *) ;;
    esac
  done
}

main
