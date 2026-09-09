---
name: commit-guidelines
description: Use when creating commits or writing commit messages to organize atomic commits and format commit messages according to project standards.
---

# Commit Guidelines

## Commit Organization
- **Atomic Commits:** Each commit should represent a single logical change. Do not mix unrelated bug fixes, refactoring, and feature additions in the same commit.
- **Logical Separation:** Separate refactoring changes from functional changes where feasible.
- **Verification:** Always inspect `git status` and `git diff` before staging and committing. Stage only intended files and never commit secrets or generated artifact files.

## Commit Message Format
- Use a clear, concise summary line in the imperative mood (e.g., "Add calorie estimation utility" instead of "Added calorie estimation utility" or "Adding...").
- Keep the summary line under 50 characters when possible.
- If needed, add a blank line followed by a more detailed explanatory body describing *what* and *why* (not *how*).
- Follow conventional commit types if applicable (e.g., `feat:`, `fix:`, `refactor:`, `docs:`, `test:`).
