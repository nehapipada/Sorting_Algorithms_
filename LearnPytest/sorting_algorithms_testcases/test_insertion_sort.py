from LearnPytest.sorting_algorithms_definition.insertion_sort import insertion_sort
import pytest
@pytest.fixture
def unsorted_list():
    return [4, 2, 7, 1, 9, 5, 3, 8, 6]



def test_insertion_sort(unsorted_list):
    s1 = insertion_sort(unsorted_list)
    assert unsorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]