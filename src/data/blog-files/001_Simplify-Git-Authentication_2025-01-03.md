# Simplify Git Authentication

Tired of entering your credentials repeatedly while working with Git? The `git config credential.helper store` command
can help!

### What It Does

This command saves your Git credentials (username and password) in a plain-text file, allowing Git to use them
automatically for future operations.

### How to Use

1. **Enable the Helper**:

   ```bash
   git config --global credential.helper store
   ```
2. **Authenticate Once**: Perform an operation (e.g., `git push`), and Git will prompt for your credentials. These will
   be saved.
3. **Location**: Credentials are stored in:
    - **Linux/Mac**: `~/.git-credentials`
    - **Windows**: `C:\Users\<YourUsername>\.git-credentials`

### Pros and Cons

- **Pros**: Convenience and speed.
- **Cons**: Credentials are stored in plain text—use only on trusted devices.

### Disable It

To remove this feature:

```bash
git config --global --unset credential.helper
```

For added security, consider using SSH keys or `credential.helper cache`.

Happy coding! 🚀
