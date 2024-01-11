class Solution(object):
    def topKFrequent(self, nums, k):
        most_frequent = {}
        
        for i in range(len(nums)):
            number = nums[i] 
            if number not in most_frequent:
                most_frequent[number] = 1
            else: 
                most_frequent[number] = most_frequent[number] + 1

        result = []

        for i in range(k):
            biggest = (most_frequent.keys())[0]
            for number in most_frequent:
                most_frequent[biggest]
                if most_frequent[number] > most_frequent[biggest]:
                    biggest = number
      
            result.append(biggest)
            del most_frequent[biggest]

        return result