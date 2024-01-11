class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(word)
            else:
                anagrams[sorted_string] = [word]
        return list(anagrams.values())