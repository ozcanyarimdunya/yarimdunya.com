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

echo "Default (10sec)"
spinner
echo ""

echo "5 second"
spinner 5
echo ""

echo "5 second with text"
spinner 5 "Continue"
echo ""
