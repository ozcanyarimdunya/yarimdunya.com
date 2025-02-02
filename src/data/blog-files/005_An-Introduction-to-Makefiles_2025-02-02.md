# Introduction to Makefiles

A **Makefile** is a simple way to automate repetitive tasks in a software project—often compilation, but it can be used
for many other tasks (e.g., running tests, building documentation, or deploying).

## Why Use Makefiles?

1. **Automation**: Easily run commands in a structured order.
2. **Dependency Management**: Only rebuild what’s changed, saving time.
3. **Standardization**: Common commands (`make all`, `make clean`, etc.) become part of your project’s workflow.
4. **Portability**: `make` is widely installed on Unix-like systems (Linux, macOS) and available on Windows through
   tools like Cygwin or MSYS.

---

# Basic Concepts

### Targets and Rules

A Makefile consists of **rules**. Each rule specifies:

- A **target** (often the name of a file to create or a phony target).
- A **prerequisite** or **dependency** (files needed to build the target).
- A **recipe** (the commands to build the target).

```makefile
target: prerequisite1 prerequisite2
    command1
    command2
```

> **Note**: The indentation before each command **must** be a tab character (not spaces).

### Phony Targets

Sometimes, you have targets that don’t represent actual files but are just commands you want to run. These are **phony
targets**:

```makefile
.PHONY: clean

clean:
    rm -rf *.o main
```

By declaring `.PHONY`, `make` won’t look for a file literally named `clean` and will always run the recipe.

### Variables

You can define variables in Makefiles to avoid repetition:

```makefile
CC = gcc
CFLAGS = -Wall -O2

main: main.o helper.o
    $(CC) $(CFLAGS) -o main main.o helper.o
```

- **`$(CC)`** will be replaced by `gcc`.
- **`$(CFLAGS)`** will be replaced by `-Wall -O2`.

### Pattern Rules (Automatic Compilation)

Make supports pattern rules to describe how to build similar types of files. For example, to compile all `.c` files to
`.o` files:

```makefile
%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

- `$<` is the first prerequisite (e.g., the `.c` file).
- `$@` is the target (e.g., the `.o` file name).

### Special Variables

- **$@**: Represents the target name.
- **$<**: Represents the first prerequisite.
- **$^**: Represents all prerequisites.
- **$?**: Represents prerequisites that are newer than the target.

---

# Minimal Example

Let’s say you have two C files, `main.c` and `helper.c`. You want to build `main`:

```makefile
CC = gcc
CFLAGS = -Wall -O2

all: main

main: main.o helper.o
    $(CC) $(CFLAGS) -o main main.o helper.o

main.o: main.c
    $(CC) $(CFLAGS) -c main.c -o main.o

helper.o: helper.c
    $(CC) $(CFLAGS) -c helper.c -o helper.o

clean:
    rm -f *.o main
```

1. **`all: main`** – The default target that depends on `main`.
2. **`main: main.o helper.o`** – Links the object files into the final executable.
3. **`main.o: main.c`** – Compiles `main.c` into object code.
4. **`helper.o: helper.c`** – Compiles `helper.c` into object code.
5. **`clean`** – Removes generated files.

Running `make` in the same directory will create the `main` executable. Running `make clean` removes the generated files
so you can start fresh.

---

# Helpful Tips

1. **Use Variables**: Storing commands and flags in variables keeps your Makefile flexible.
2. **Use Pattern Rules**: When you have many source files, pattern rules drastically reduce duplication:
   ```makefile
   %.o: %.c
       $(CC) $(CFLAGS) -c $< -o $@
   ```
3. **Use `.PHONY`**: For targets that don’t produce files:
   ```makefile
   .PHONY: clean
   clean:
       rm -f *.o main
   ```
4. **Split Makefiles**: For larger projects, consider using multiple Makefiles or including common fragments:
   ```makefile
   include common.mk
   ```
5. **Use Implicit Variables**: GNU Make has built-in variables like `CC` for C compiler, `CXX` for C++ compiler, etc.
6. **`make -jN`**: Parallelizes builds (where **N** is the number of jobs). E.g., `make -j4` speeds up the build by
   using 4 processes.

---

# Common Commands

- **`make`**: Builds the default (or first) target in the Makefile.
- **`make <target>`**: Builds a specific target (e.g., `make clean`).
- **`make -n`**: Shows what commands would be executed without actually running them.
- **`make -j`**: Runs multiple jobs in parallel.
- **`make VERBOSE=1`**: In some projects, displays detailed commands (if the Makefile is set up to respond to VERBOSE).

---

# Conclusion

A Makefile is a powerful yet straightforward tool for defining how to build, test, and clean your projects. By mastering
the basics—targets, recipes, variables, and pattern rules—you can streamline your build process and ensure consistency
across your team or across different machines.

**Key takeaway**: At its core, a Makefile is just a list of **targets**, their **dependencies**, and the **commands** (
recipes) to generate them. Once you grasp that concept, you can extend it to automate various tasks beyond just
compilation—like running tests, packaging, or even documentation generation.

---
