# NovaSolve Flask Demo Repo (Validation)

This is a small, credible demo repo designed to showcase NovaSolve turning failing tests (red) to passing (green) by fixing three realistic bugs:

- Logic miscalculation (tax application)
- Off-by-one loop boundary
- Missing `None` check causing an exception

It includes a tiny Flask surface (optional) to add realism, but tests focus on pure Python functions for speed and determinism.

## Structure

```
validation/flask-demo-repo/
  README.md
  requirements.txt
  src/
    __init__.py
    core.py        # intentionally buggy
    web.py         # minimal Flask app using core.py (optional)
  tests/
    __init__.py
    test_core.py   # fails red until fixed
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run tests (Red)

```bash
pytest -q
```

Expected initial failures:

- calc_total uses addition instead of multiplicative tax → wrong total
- process_items skips the final element → missing output
- admin_action crashes on `None` user → AttributeError

## Run NovaSolve

From this folder, run NovaSolve to autonomously fix the issues. Examples:

```bash
# Autopilot (non-interactive) with a strong model
nova solve . --model gpt-4o

# Manual approval to show diffs/rationale for at least one fix
nova solve . --model gpt-4o --manual-approval
```

Notes:

- Ensure `OPENAI_API_KEY` (or your configured provider) is set.
- Ensure your working tree is clean so NovaSolve can branch/commit safely.

## Verify (Green)

```bash
pytest -q
```

All tests should pass after NovaSolve applies fixes.

## Bugs (for reference)

1) Logic error in `calc_total`: uses `subtotal + tax_rate` instead of `subtotal * (1 + tax_rate)`.
2) Off-by-one in `process_items`: loops to `len(items) - 1`, skipping last element.
3) Missing `None` check in `admin_action`: calls `user.is_admin` when `user` can be `None`.

These are realistic, high-signal bugs that produce clear test failures and minimal diffs when fixed.


# demo
