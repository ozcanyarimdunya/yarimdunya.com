# Pipe

# Piping

```shell
#!/bin/bash
:'
USAGE
-----
1) cat test.txt | ./pipe.sh
2) ./pipe.sh < test.txt
'

while read line; do
  echo $line;
done
```
