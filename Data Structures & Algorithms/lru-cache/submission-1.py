class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=True) #move to right bc used
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key, last=True) #move to right bc used
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value 
            else: #so if over
                self.cache.popitem(last=False) #remove left item
                self.cache[key] = value 
        


        
#input: cache inputs lol
#init cache and capacity params
#implement get to check for key or return -1 if doesnt exist
#implement put to update val of key, add key, and potentially replace last used key

#used meaning called by get or put
#so need to use ordereddict and implement our own system
#so if you use something, move it to the right
#then just pop an item from the left if you have to replace
