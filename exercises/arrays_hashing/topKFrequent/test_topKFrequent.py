from topKFrequent import Solution

def test_topKFrequent():
    sol = Solution()
    assert sol.topKFrequent([1,1,1,2,2,3], 2) == [1, 2]

def test_topKFrequent2():
    sol = Solution()
    assert sol.topKFrequent([1], 1) == [1]