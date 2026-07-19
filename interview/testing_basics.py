from unittest.mock import Mock, patch

# This repo has no pytest installed (intentionally -- see CLAUDE.md, it's a
# script-based practice repo, not a package with a test suite). The pieces
# below are explained in comments since they can't be run without the
# dependency; the mocking demo further down uses unittest.mock, which is
# stdlib and needs no install, so that part is fully runnable.

# --- pytest fundamentals (conceptual -- not runnable here) ------------------
#
# - A test is just a function named test_* in a file named test_*.py or
#   *_test.py. No class or decorator required (unittest.TestCase style with
#   assertEqual etc. also works, but pytest's plain-function style is the
#   more common idiom).
#
# - `assert` is the whole assertion mechanism: no assertEqual/assertTrue
#   zoo needed. pytest rewrites the `assert` statement at import time to
#   capture both sides of the comparison, so a failure like
#   `assert result == expected` prints the actual values on both sides
#   instead of just "AssertionError".
#
#     def test_add():
#         assert add(2, 3) == 5
#
# - Fixtures (`@pytest.fixture`) provide setup/teardown and shared test
#   data via dependency injection: a test function just declares a
#   parameter with the fixture's name and pytest supplies the value. This
#   is the direct test-world analogue of the context managers studied in
#   context_managers.py -- a fixture using `yield` runs the code before
#   `yield` as setup and after `yield` as teardown, guaranteed to run even
#   if the test fails, same as __exit__ always running.
#
#     @pytest.fixture
#     def db_connection():
#         conn = connect()
#         yield conn          # this is what the test receives
#         conn.close()        # teardown, runs even if the test raises
#
#     def test_query(db_connection):
#         assert db_connection.execute("SELECT 1") == 1
#
# - `@pytest.mark.parametrize` runs the same test body against multiple
#   input/expected pairs, so you don't copy-paste near-identical tests:
#
#     @pytest.mark.parametrize("value,expected", [(1, 1), (2, 4), (3, 9)])
#     def test_square(value, expected):
#         assert square(value) == expected

print("pytest fundamentals: see comments above (no pytest dependency in this repo)")
print("---")


# --- Mocking (runnable -- unittest.mock is stdlib) --------------------------
#
# The point of mocking: replace a real (slow, external, or side-effecting)
# dependency with a stand-in you fully control, so the test exercises only
# your code's logic, not the network/disk/API it happens to call.

def send_email(client, to, subject):
    # imagine `client` is a real SMTP/API client with a network call inside
    client.send(to=to, subject=subject)
    return True


# Mock() creates an object that accepts any attribute access or call and
# just records it -- no real class needed. Every call is logged so you can
# assert on it afterward.
fake_client = Mock()
result = send_email(fake_client, "a@example.com", "hi")

fake_client.send.assert_called_once_with(to="a@example.com", subject="hi")
print("assert_called_once_with passed -- send_email called the client correctly")
print("return value:", result)

print("---")


def get_discounted_price(pricing_service, product_id):
    base_price = pricing_service.fetch_price(product_id)
    return base_price * 0.9


# .return_value stubs what a mock call produces, so you can test logic that
# depends on an external result without that dependency actually existing.
fake_pricing = Mock()
fake_pricing.fetch_price.return_value = 100
print("discounted price:", get_discounted_price(fake_pricing, "sku-1"))

print("---")


# patch() temporarily replaces a real object (usually looked up by
# "where it's used", not "where it's defined") for the duration of the
# `with` block, then restores the original -- useful when the dependency
# is imported directly by the module under test rather than passed in as
# an argument (i.e. you can't just substitute a Mock via a function param).
import time as time_module


def slow_operation():
    time_module.sleep(5)
    return "done"


with patch("time.sleep") as mock_sleep:
    print(slow_operation())          # doesn't actually sleep for 5 seconds
    mock_sleep.assert_called_once_with(5)
    print("assert_called_once_with passed -- time.sleep was faked, not really run")
