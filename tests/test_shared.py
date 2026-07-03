import pytest

from json_logic import UNDEFINED_VALUE, jsonLogic


@pytest.mark.unsupported_operators(["filter", "all", "none", "some"])
@pytest.mark.unsupported_logic(
    [
        {"var": []},
    ]
)
def test_shared_test(shared_test):
    """
    Test the shared JSON tests one-by-one.

    ``logic`` combined with ``data`` must yield ``expected`` result.
    """
    logic, data, expected = shared_test

    result = jsonLogic(logic, data)

    assert result == expected


@pytest.mark.unsupported_operators(["filter", "all", "none", "some"])
@pytest.mark.unsupported_logic(
    [
        {"var": []},
    ]
)
def test_shared_test_with_undefined_var(shared_test):
    """
    Test the shared JSON tests one-by-one.

    ``logic`` combined with ``data`` must yield ``expected`` result.
    """
    logic, data, expected = shared_test

    result = jsonLogic(logic, data, use_var_undefined=True)

    # no access to the external tests which adhere to None for empty values
    if result is UNDEFINED_VALUE:
        result = None

    assert result == expected
