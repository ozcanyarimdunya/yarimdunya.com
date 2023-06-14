# Bash Utilities

## Log utility

```python
{!codes/bash/utils.sh!}
```

### Usage

![bash-utils.png](./images/bash-utils.png)


### Multiple command executions


```shell
for i in {1..5} ; do
    (sleep "$i" && echo "worker $i finished") &
    (sleep "$i" && echo "worker -$i finished") &
    (sleep "$i" && echo "worker --$i finished") &
done
```
