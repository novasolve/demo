import os
import sys
import pytest

# Ensure src/ is importable
CURRENT_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
sys.path.insert(0, SRC_PATH)

from core import admin_action, calc_total, process_items, User  # noqa: E402


def test_calc_total_expected_formula():
    # Expect subtotal * (1 + tax_rate)
    assert calc_total(100.0, 0.08) == pytest.approx(108.0)
    assert calc_total(0.0, 0.2) == pytest.approx(0.0)
    assert calc_total(50.0, 0.0) == pytest.approx(50.0)


def test_process_items_includes_last_element():
    items = [1, 2, 3, 4, 5]
    # Expect doubling all elements
    assert process_items(items) == [2, 4, 6, 8, 10]


def test_admin_action_handles_none_user():
    # Should not raise; should return "forbidden" for anonymous user
    assert admin_action(None) == "forbidden"


def test_admin_action_admin_ok():
    user = User(is_admin=True, is_authenticated=True)
    assert admin_action(user) == "ok"
