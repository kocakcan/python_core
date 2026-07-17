# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a personal Python learning/practice repository — not a library, application, or package. There is no build system, no dependency manifest (no `requirements.txt`/`pyproject.toml`), and no test runner configured. Files are standalone scripts used to study language features, often written while working through a course or self-study curriculum, plus material for interview preparation.

Do not introduce packaging, a test framework, linting config, or CI unless explicitly asked — the repo intentionally stays dependency-free and script-based.

## Running code

There's no single entry point. Run any file directly:

```bash
python3 code/<file>.py
```

Most scripts are self-contained and executable top-to-bottom (many `print()` calls used to inspect behavior in the terminal rather than assertions). Some files contain commented-out alternate versions of the same code left in place intentionally, showing "before/after" or "buggy vs fixed" variants for study purposes (e.g. `interview/memory_management.py`'s mutable-default-argument example, `code/m4_functions/l9c.py`'s nested decorators). Don't "clean up" these comments unless asked — they're the point of the file.

## Structure

- `code/` — general Python language study scripts, one topic per file (e.g. `iterator.py`, `generator.py`, `dict_methods.py`, `list_comprehensions.py`, `namedtuple.py`).
  - `code/m4_functions/`, `code/m5_modules_and_packages/`, `code/m6_oop/` — numbered module directories from a structured course, with lesson files named `l0.py`, `l1.py`, `l2.py`, ... in teaching order. Higher lesson numbers build on concepts from lower ones in the same directory.
  - `code/first_test.robot` — a Robot Framework browser UI test suite (uses the `Browser` library) against the public TodoMVC React demo app. Unrelated to the Python study material; requires `robotframework-browser` installed and its `rfbrowser init` browser binaries set up to run.
- `interview/` — interview-preparation material (round-specific prep notes in `prep.md`, plus scratch exercises like `exercise.py`, `generators_and_iterators.py`, `memory_management.py` written to rehearse explaining Python internals out loud).
- `song.txt` — unrelated text content, not part of the codebase.

## Working in this repo

- When adding a new study script, match the existing style: short standalone file, comments explaining the *why* of a language behavior, `print()`-driven demonstration rather than `assert`/test framework.
- When adding to a numbered module directory (`m4_functions`, `m5_modules_and_packages`, `m6_oop`), follow the existing `lN.py` naming/ordering convention.
- `interview/prep.md` is a living checklist tied to a specific upcoming interview — treat checkbox state and scheduling notes there as current and update them in place rather than rewriting the file's structure.
