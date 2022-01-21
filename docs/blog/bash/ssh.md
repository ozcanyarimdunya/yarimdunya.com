# Ssh connection

1. `ssh username@server`
2. `ssh username@groupname@jumpserver server`


## Ssh without password

**sshpass**

Download sshpass [link](https://sourceforge.net/projects/sshpass/files/sshpass/)

```
cd folder
./configure
make install
```

> with password 

```shell
sshpass -p your-pwd ssh username@server

sshpass -p your-pwd scp -r username@server:/tmp/* ~/Desktop/
```

> with password file

```shell
echo your-pwd > /tmp/pwd.txt

sshpass -f /tmp/pwd.txt ssh username@server

sshpass -f /tmp/pwd.txt scp -r username@server:/tmp/* ~/Desktop/
```

> with a user
 
```shell
ssh -l user username@server
```
