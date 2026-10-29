# daytona-demo-repo

A tiny Python project used as the "customer codebase" in a Daytona demo.
Build agents clone it into sandboxes, make changes on task branches, run the
tests, and push.

## Run the tests

```bash
pip install pytest
pytest
```

## Example subtasks for agents

1. Add `power(base, exp)` to `calc/operations.py` with tests.
2. Add `modulo(a, b)` to `calc/operations.py` (raise `ZeroDivisionError` on `b == 0`) with tests.
3. Add `is_palindrome(text)` to `calc/strings.py` with tests.
4. Add `word_count(text)` to `calc/strings.py` with tests.
