def containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    newArray = []
    original = {}
    for idx, value in enumerate(nums):
        original[value] = idx
    nums.sort()
    
    
        
        