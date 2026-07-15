# Test Report — Mergington High School API

**Date:** 2026-07-15  
**Project:** `tech-skills-getting-started-with-github-copilot`  
**Branch:** `main`  
**Test suite:** `tests/test_app.py`  
**Framework:** pytest 9.1.1 · Python 3.13.14  

---

## Summary

| Metric | Value |
|---|---|
| Total tests | 12 |
| Passed | 12 |
| Failed | 0 |
| Errors | 0 |
| Warnings | 1 |
| Duration | 0.13 s |

**Result: ✅ ALL TESTS PASSED**

---

## Results by Endpoint

### `GET /`

| Test | Result |
|---|---|
| `test_root_redirects_to_index` | ✅ PASSED |

### `GET /activities`

| Test | Result |
|---|---|
| `test_get_activities_returns_200` | ✅ PASSED |
| `test_get_activities_returns_all_activities` | ✅ PASSED |
| `test_get_activities_each_has_required_fields` | ✅ PASSED |

### `POST /activities/{activity_name}/signup`

| Test | Result |
|---|---|
| `test_signup_success` | ✅ PASSED |
| `test_signup_adds_participant` | ✅ PASSED |
| `test_signup_duplicate_returns_400` | ✅ PASSED |
| `test_signup_unknown_activity_returns_404` | ✅ PASSED |

### `DELETE /activities/{activity_name}/participants`

| Test | Result |
|---|---|
| `test_unregister_success` | ✅ PASSED |
| `test_unregister_removes_participant` | ✅ PASSED |
| `test_unregister_not_signed_up_returns_404` | ✅ PASSED |
| `test_unregister_unknown_activity_returns_404` | ✅ PASSED |

---

## Warnings

| # | Warning |
|---|---|
| 1 | `StarletteDeprecationWarning`: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead. |

> This warning does not affect test results. It can be resolved by replacing `httpx` with `httpx2` in `requirements.txt`.

---

## Raw Output

```
============================= test session starts ==============================
platform linux -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
rootdir: /workspaces/tech-skills-getting-started-with-github-copilot
configfile: pytest.ini
plugins: anyio-4.14.2
collected 12 items

tests/test_app.py::test_root_redirects_to_index PASSED                   [  8%]
tests/test_app.py::test_get_activities_returns_200 PASSED                [ 16%]
tests/test_app.py::test_get_activities_returns_all_activities PASSED     [ 25%]
tests/test_app.py::test_get_activities_each_has_required_fields PASSED   [ 33%]
tests/test_app.py::test_signup_success PASSED                            [ 41%]
tests/test_app.py::test_signup_adds_participant PASSED                   [ 50%]
tests/test_app.py::test_signup_duplicate_returns_400 PASSED              [ 58%]
tests/test_app.py::test_signup_unknown_activity_returns_404 PASSED       [ 66%]
tests/test_app.py::test_unregister_success PASSED                        [ 75%]
tests/test_app.py::test_unregister_removes_participant PASSED            [ 83%]
tests/test_app.py::test_unregister_not_signed_up_returns_404 PASSED      [ 91%]
tests/test_app.py::test_unregister_unknown_activity_returns_404 PASSED   [100%]

======================== 12 passed, 1 warning in 0.13s =========================
```
