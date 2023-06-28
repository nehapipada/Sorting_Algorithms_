from LearnPytest.sorting_algorithms_definition.merge_sort import merge_sort
import pytest
@pytest.fixture
def unsorted_list():
    return [4, 2, 7, 1, 9, 5, 3, 8, 6]


def test_merge_sort(unsorted_list):
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list