
from copy import deepcopy

from sorting import *
from getRadomData import *

class TestSorting(object):
    def setup(self):
        self.scale = 5
        self.lists = getRadomData(self.scale )
        
    def teardown(self):
        self.scale = None
        self.lists = None
        
    def test_insert_sort_min(self):
        min_element = min(self.lists)
        print min_element
        print self.lists
        assert bubble_sort(self.lists)[0] == min_element        
        
    def test_insert_sort_max(self):
        max_element = max(self.lists)
        print max_element
        print self.lists
        assert bubble_sort(self.lists)[-1] == max_element
        
    def test_insert_sort_all(self):
        tmp_lists = deepcopy(self.lists)
        sorted_lists = sorted(tmp_lists)
        print sorted_lists
        bubble_sort(self.lists)
        print self.lists
        assert sorted_lists == self.lists
        
    def test_integration_of_sorted_lists(self):
        tmp_lists = deepcopy(self.lists)
        bubble_sort(self.lists)
        print tmp_lists
        print self.lists
        for val in tmp_lists:
            assert val in self.lists

"""
    def test_insert_sort_min(self):
        min_element = min(self.lists)
        assert insert_sort(self.lists)[0] == min_element
        
    def test_insert_sort_max(self):
        max_element = max(self.lists)
        assert insert_sort(self.lists)[-1] == max_element
        
    def test_insert_sort_all(self):
        tmp_lists = self.lists
        sorted(tmp_lists)
        insert_sort(self.lists) 
        assert tmp_lists == self.lists
        
    def test_integration_of_sorted_lists(self):
        tmp_lists = self.lists
        intsert_sort(self.lists)
        for val in tmp_lists:
            assert val in self.lists
"""
