import pytest
from contextlib import nullcontext as does_not_raise 
from src.funcs import add, add_to_list, divide


@pytest.fixture
def get_list():
    return ["Alice", "Bob", "Charlie"]


@pytest.fixture
def get_other_list():
    return [1, 2, 3]


@pytest.fixture
def get_mega_list(get_list, get_other_list):
    return [get_list, get_other_list]



# @pytest.mark.parametrize(
#     "a, b, expected_result, expected_context",
#     [
#         (2, 2, 4, does_not_raise()),
#         (2, 3, 5, does_not_raise()),
#         # (2, 5, 6, does_not_raise()),
#         (2, 4, 6, does_not_raise()),
#         ("2", 3, None, pytest.raises(TypeError)),
#     ]
# )
# def test_add(a, b, expected_result, expected_context):
#     with expected_context:
#         assert add(a, b) == expected_result



# @pytest.mark.parametrize(
#     "fixture_name, addition, expected_result, expected_context",
#     [
#         ("get_list", "Dani", ["Alice", "Bob", "Charlie", "Dani"], does_not_raise()),
#         ("get_other_list", 4, [1, 2, 3, 4], does_not_raise()),
#         ("get_mega_list", 2.0, [["Alice", "Bob", "Charlie"], [1, 2, 3], 2.0], does_not_raise())
#     ]
# )
# def test_add_list(request, fixture_name, addition, expected_result, expected_context):
#     with expected_context:
#         inp_list = request.getfixturevalue(fixture_name)
#         assert add_to_list(inp_list, addition) == expected_result


@pytest.mark.parametrize(
    "a, b, expected_result, expected_context",
    [
        (4, 2, 2, does_not_raise()),
        (10, 5, 2, does_not_raise()),
        (9, 3, 3, does_not_raise()),
        (1, 0, None, does_not_raise()),
        ("3", "1", None, pytest.raises(TypeError)),
    ]
)
def test_divide(a, b, expected_result, expected_context):
    with expected_context:
        assert divide(a, b) == expected_result