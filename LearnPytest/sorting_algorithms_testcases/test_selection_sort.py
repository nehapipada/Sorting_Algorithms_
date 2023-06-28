from LearnPytest.sorting_algorithms_definition.selection_sort import selection_sort
import pytest
@pytest.fixture
def unsorted_list():
    return [4, 2, 7, 1, 9, 5, 3, 8, 6]


def test_selection_sort(unsorted_list):
    s1 = selection_sort(unsorted_list)
    assert s1 == [1, 2, 3, 4, 5, 6, 7, 8, 9]
#selection_sort