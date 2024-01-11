from groupAnagrams import Solution

def test_groupAnagrams():
    sol = Solution()
    result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    # Convert lists of lists to sets of frozensets
    result_set = set(frozenset(group) for group in result)
    expected_set = set(frozenset(group) for group in expected)

    assert result_set == expected_set

def test_groupAnagrams2():
    sol = Solution()
    result = sol.groupAnagrams([""])
    expected = [[""]]

    assert result == expected

def test_groupAnagrams3():
    sol = Solution()
    result = sol.groupAnagrams(["a"])
    expected = [["a"]]

    assert result == expected