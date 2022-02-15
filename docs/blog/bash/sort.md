# Sort 


**test.txt**

```text
X 1 3
Y 2 5
A 5 2
```

## Default

**Command**

```shell
cat test.txt | sort
```

**Output**

```text
A 5 2
X 1 3
Y 2 5
```

## Sort by column 

**Command**

```shell
cat test.txt | sort -k 2
```

**Output**

```text
X 1 3
Y 2 5
A 5 2
```
