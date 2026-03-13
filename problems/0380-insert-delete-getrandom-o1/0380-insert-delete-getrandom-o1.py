import random
class RandomizedSet:
    
    def __init__(self):
        self.nums = []
        self.nums2index = {}

    def insert(self, val: int) -> bool:
        if val in self.nums2index:
            return False
        else:
            self.nums.append(val)
            self.nums2index[val] = len(self.nums) - 1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.nums2index:
            return False
        else:
            index = self.nums2index[val]
            n = self.nums[-1]
            self.nums2index[n] = index
            self.nums[index] = n
            self.nums.pop()
            self.nums2index.pop(val)
            return True
        

    def getRandom(self) -> int:
        x = random.randint(0, len(self.nums) - 1)
        return self.nums[x]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()