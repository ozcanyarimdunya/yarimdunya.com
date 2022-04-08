#!/usr/bin/env bash

success() {
  echo -e "\e[1;32m$1\e[0m"
}

info() {
  echo -e "\e[1;34m$1\e[0m"
}

warn() {
  echo -e "\e[1;33m$1\e[0m"
}

error() {
  echo -e "\e[1;31m$1\e[0m"
}

ask() {
  while true; do
    read -p "→ $1 (y/n) ? " answer
    case ${answer} in
      [Yy]*) return 0 ;;
      [Nn]*) return 1 ;;
      *) error "Please answer y/Y or n/N" ;;
    esac
  done
}


info "Program started."
warn "Prepare for the prompt"

if ask "Are you sure"; then
  success "Yes, I am sure!"
else
  error "No, I am not sure!"
fi

info "Program completed."
error "You are going to offline mode!"

