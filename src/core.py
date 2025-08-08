from typing import Iterable, List, Optional


def calc_total(subtotal: float, tax_rate: float) -> float:
    """Calculate total including tax.

    BUG: incorrectly adds tax_rate directly to subtotal.
    Expected: subtotal * (1 + tax_rate)
    """
    return subtotal + tax_rate  # BUG


def process_items(items: Iterable[int]) -> List[int]:
    """Process a list of items; here we simply double each value.

    BUG: off-by-one error skips the final element.
    Expected: process all elements.
    """
    items_list = list(items)
    processed: List[int] = []
    for i in range(len(items_list) - 1):  # BUG: skips last item
        processed.append(items_list[i] * 2)
    return processed


class User:
    def __init__(self, is_admin: bool = False, is_authenticated: bool = False) -> None:
        self._is_admin = is_admin
        self.is_authenticated = is_authenticated

    def is_admin(self) -> bool:
        return self._is_admin


def admin_action(user: Optional["User"]) -> str:
    """Return action result for user.

    BUG: missing None check; AttributeError if user is None.
    Expected: handle None and return "forbidden" instead of crashing.
    """
    if user.is_admin():  # BUG: no None guard
        return "ok"
    return "forbidden"
