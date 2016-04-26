from searching import *
from getRadomData import getRadomData


class TestSearching:
    def setup(self):
        self.scale = 4
        self.lists = getRadomData(self.scale)
        self.lists.sort()
        print self.lists
        self.targetGreatThanMax = 200
        self.targetLessThanMin = -100
        
    def teardown(self):
        self.scale = 0
        self.lists = None
        
    """Test linear search"""
    def test_sorted_linear_search_1st(self):
        assert sortedLinearSearch(self.lists[0], self.lists) == True
        
    def test_sorted_linear_search_last(self):
        assert sortedLinearSearch(self.lists[-1], self.lists) == True    
        
    def test_sorted_linear_search_min(self):
        assert sortedLinearSearch(min(self.lists), self.lists) == True       
        
    def test_sorted_linear_search_max(self):
        assert sortedLinearSearch(max(self.lists), self.lists) == True    
        
    #target NOT in list: search failed
    def test_sorted_linear_search_great_than_max(self):
        assert sortedLinearSearch(self.targetGreatThanMax, self.lists) == False
        
    def test_sorted_linear_search_less_than_mix(self):
        assert sortedLinearSearch(self.targetLessThanMin, self.lists) == False
        
    """Test binary search"""
    def test_sorted_binary_search_1st(self):
        assert binarySearch(self.lists[0], self.lists) == True
        
    def test_sorted_binary_search_last(self):
        assert binarySearch(self.lists[-1], self.lists) == True    
        
    def test_sorted_binary_search_min(self):
        assert binarySearch(min(self.lists), self.lists) == True       
        
    def test_sorted_binary_search_max(self):
        assert binarySearch(max(self.lists), self.lists) == True   
        
    #target NOT in list: search failed
    def test_stored_binary_search_great_than_max(self):
        assert binarySearch(self.targetGreatThanMax, self.lists) == False
        
    def test_stored_binary_search_less_than_min(self):
        assert binarySearch(self.targetLessThanMin, self.lists) == False
        