# Readme

This repository contains a simple pre-commit hook that for a `// for ` comment
right after an `#include` statement in C++ source code.

## Usage

Add it to your `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/SalvoVirga/pre-commit-hook-cpp-for-comment-on-include
    rev: v1.0.0
    hooks:
      - id: cpp-for-comment-on-include
```