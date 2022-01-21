# Tar commands

## Extract

```shell
tar -xf archive.tar.gz
```

## Compress

```shell
tar -czf archive.tar.gz file1 file2
```


---

## Tar Command Syntax

```shell
tar [OPERATION_AND_OPTIONS] [ARCHIVE_NAME] [FILE_NAME(s)]
```

**OPERATION**  

Only one operation argument is allowed and required. The most frequently used operations are:

- `--create (-c) `- Create a new tar archive.
- `--extract (-x)` - Extract the entire archive or one or more files from an archive.
- `--list (-t)` - Display a list of the files included in the archive

**OPTIONS** 

The most frequently used operations are:

- `--verbose (-v)` - Show the files being processed by the tar command.
- `--file=archive=name (-f archive-name)` - Specifies the archive file name.

**ARCHIVE_NAME** 

The name of the archive.

**FILE_NAME(s)** 

A space-separated list of filenames to be extracted from the archive. If not provided, the entire archive is extracted.


## Examples
 
### Create tar

```shell
tar -cf archive.tar file1 file2 file3

tar --create --file=archive.tar file1 file2 file3

tar -cf backup.tar /home/user

# tar.gz
tar -czf archive.tar.gz file1 file2

# tar.bz2
tar -cjf archive.tar.bz2 file1 file2
```

### List tar

```shell
tar -tf archive.tar

# output
file1   
file2
file3

tar -tvf archive.tar

# output
-rw-r--r-- linuxize/users       0 2018-09-08 01:19 file1
-rw-r--r-- linuxize/users       0 2018-09-08 01:19 file2
-rw-r--r-- linuxize/users       0 2018-09-08 01:19 file3
```

### Extract Tar

```shell
tar -xf archive.tar

tar -xvf archive.tar

tar -xf archive.tar -C /opt/files

tar -xf archive.tar.gz

tar -xf archive.tar.bz2

# extract specific files
tar -xf archive.tar file1 file2

# extract some other files
tar -xf archive.tar --wildcards '*.js'

# append new file
tar -rvf archive.tar newfile

# remove files
tar --delete -f archive.tar file1
```
