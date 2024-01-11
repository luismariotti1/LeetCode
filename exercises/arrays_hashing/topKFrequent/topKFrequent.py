class Solution(object):
    def topKFrequent(self, nums, k):
        most_frequent = {}
        
        for num in nums:
            if num not in most_frequent:
                most_frequent[num] = 1
            else:
                most_frequent[num] += 1

        result = []

        for _ in range(k):
            biggest = list(most_frequent.keys())[0]
            for number in most_frequent:
                if most_frequent[number] > most_frequent[biggest]:
                    biggest = number
      
            result.append(biggest)
            del most_frequent[biggest]

        return result
