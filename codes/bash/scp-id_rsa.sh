#!/usr/bin/env bash

# Check if user is not root
[[ "$(whoami)" == "root" ]] && echo "Do not run with root user!" && exit 1

USERNAME=$(whoami)
SERVERS=(
  "10.10.10.10"
  "10.10.10.11"
  "10.10.10.12"
  "10.10.10.13"
)
PUB_FOLDER="id-rsa-pub-files"

read -r -d '' COMMAND << EOM
/usr/bin/ssh-keygen -t rsa
chmod 600 ~/.ssh/id_rsa
EOM

rm -rf "${PUB_FOLDER}"
mkdir "${PUB_FOLDER}" 

for server in "${SERVERS[@]}" ; do
  echo -e "\n************ ${server} ************\n"
  # copy ssh-key
  ssh-copy-id -f "${USERNAME}@${server}"

  # Run 'generate key' and 'change mod' command on server
  ssh "${USERNAME}@${server}" "${COMMAND}"

  # Copy 'id_rsa.pub' file to local
  scp "${USERNAME}@${server}:/home/${USERNAME}/.ssh/id_rsa.pub" "${PUB_FOLDER}/${server}.id_rsa.pub"
done

echo "Pub files downloaded to ${PUB_FOLDER}"
