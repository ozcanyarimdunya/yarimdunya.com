### Managing Old Files with `find`: Quick Guide

The `find` command is a powerful tool for file management. Here’s a quick guide to efficiently locate, analyze, and
clean up old `tmp.txt` files.

---

#### **1. Listing Old Files**

Find and list `tmp.txt` files modified more than 5 days ago:

```bash
find . -type f -mtime +5 -name "*tmp.txt" -exec ls -la {} \;
```

**Explanation:**  
This command finds the files and uses `ls -la` to display detailed information, helping you identify unused files.

---

#### **2. Calculating Total Size**

Determine the total size of these old files:

```bash
find . -type f -mtime +5 -name "*tmp.txt" -exec du -b {} + | awk '{sum += $1} END {print sum " bytes"}'
```

**Explanation:**  
It sums up the sizes of matching files, useful for monitoring disk usage.

---

#### **3. Deleting Old Files**

Remove the identified files safely:

```bash
find . -type f -mtime +5 -name "*tmp.txt" -exec rm -f {} \;
```

**Caution:** Always preview files with `ls` before deletion to avoid mistakes.

---

### Best Practices

- Test commands with `echo` before execution.
- Use scripts for regular maintenance.
- Ensure proper permissions to avoid errors.

With these commands, you can keep your system clean and organized. Try them out and optimize your workflows!

Happy cleaning! 🧹
