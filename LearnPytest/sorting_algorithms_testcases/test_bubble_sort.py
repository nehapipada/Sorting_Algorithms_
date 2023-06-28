import sys
from LearnPytest.sorting_algorithms_definition.bubble_sort import bubblesort
import pytest
@pytest.fixture
def unsorted_list():
    return [4, 2, 7, 1, 9, 5, 3, 8, 6]
#test bubble_sort

def test_bubble_sort(unsorted_list):
    s1 = bubblesort(unsorted_list)
    assert s1 == [1, 2, 3, 4, 5, 6, 7,8, 9]