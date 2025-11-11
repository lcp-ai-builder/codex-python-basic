# Repository Guidelines

## Project Structure & Module Organization
Application code lives under `src/`; the main entry point is `src/app.py`, and additional modules should mirror their package paths (for example, `src/services/notifier.py`). Tests sit in `tests/` and follow the same package structure as the code they cover (e.g., `tests/services/test_notifier.py`). Project metadata and tooling live in `pyproject.toml`, while runtime dependencies are pinned in `requirements.txt`. Use `README.md` for quick-start context and update it whenever the developer workflow changes.

## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate`: create and activate the local virtualenv.
- `pip install -r requirements.txt`: install runtime plus dev tooling.
- `python -m src.app`: run the sample app end-to-end; add module flags here for debugging.
- `pytest -q`: execute the full test suite with concise output.
- `ruff check src tests` / `ruff format src tests`: lint and format using the repo’s configuration.

## Coding Style & Naming Conventions
Target Python 3.11 and default to four-space indents. Ruff enforces 100-character lines, double quotes, LF endings, and lint rules `E`, `F`, `I`, and `B`; run it locally before opening a PR. Name modules with lowercase snake_case, classes in PascalCase, functions and variables in snake_case, and constants in ALL_CAPS. Keep public functions documented with short docstrings describing intent and return values.

## Testing Guidelines
Write Pytest unit tests alongside the code under test; file names should start with `test_` and use descriptive function names such as `test_get_message_handles_whitespace`. Mock external services and keep assertions focused on observable behavior. Strive to touch every branch of `src/` modules; add regression tests whenever bugs are fixed. Use `pytest -vv` for focused debugging and keep fixtures in `tests/conftest.py` when they are shared.

## Commit & Pull Request Guidelines
Commit history is intentionally simple (`Initial commit`), so maintain concise, imperative subjects (`Add greeting customizer`) and include a short body when context is needed. Each PR should: link to the tracked issue, describe design decisions, list testing commands, and attach screenshots for user-facing changes. Keep PRs scoped to a single concern so reviewers can run `pytest` and `ruff check` quickly before merging.

## Security & Configuration Notes
Never commit secrets or `.venv` artifacts; store environment variables in an untracked `.env` file and load them via `os.environ`. Review dependencies before adding them to `requirements.txt`, and prefer standard-library features when possible. Keep local environments patched (`python -m pip install --upgrade pip`) to align with CI expectations.
