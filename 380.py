import random

class RandomizedSet:

    def __init__(self):

        # O(1) find, insert and remove operation 
        # provided by Python dict
        self.values = dict()

        # a mapping storage to access value indices of values in values_arr
        self.value_indices = dict()

        # values are stored in array for random pick 
        self.values_arr = []
        
    
    def insert(self, val: int) -> bool:
        
        # val is added to `values`
        if val not in self.values: 
            self.values[val] = True
            self.values_arr.append(val)
            self.value_indices[val] = len(self.values_arr) - 1
            return True
        
        return False
            

    def remove(self, val: int) -> bool:
        
        if val in self.values:

            # get its index to remove it from array 
            idx = self.value_indices[val]

            # move the last element to its place 
            # update its value in other look-ups
            last_idx = len(self.values_arr) - 1
            if idx != last_idx: 
                self.values_arr[idx] = self.values_arr[last_idx]
                last_elem = self.values_arr[last_idx]
                self.value_indices[last_elem] = idx

            self.values_arr.pop()
            del self.value_indices[val]
            del self.values[val]
            return True
        
        return False
        
        

    def getRandom(self) -> int:
        r = random.randint(0, len(self.values_arr)-1)
        value = self.values_arr[r]
        return value
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()