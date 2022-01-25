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

### with password

```shell
sshpass -p your-pwd ssh username@server

sshpass -p your-pwd scp -r username@server:/tmp/* ~/Desktop/
```

### with password file

```shell
echo your-pwd > /tmp/pwd.txt

sshpass -f /tmp/pwd.txt ssh username@server

sshpass -f /tmp/pwd.txt scp -r username@server:/tmp/* ~/Desktop/
```

### with a user

```shell
ssh -l user username@server
```


### multi line command execution

=== "with local variables"

    ```shell
    localVar="test"
    read -r -d '' command << EOM
    echo "${localVar}"
    cd /remote/path
    git pull
    process=\$(ls -la | awk '{print \$1}')
    echo "\${process}"
    EOM
    
    ssh username@server "${command}"
    ```


=== "without local variables" 

    ```shell
    ssh username@server << 'ENDSSH'
    cd /remote/path
    git pull
    process=$(ls -la | awk '{print $1}')
    echo "${process}"
    ENDSSH
    ```
