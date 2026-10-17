class MyHashMap:

    def __init__(self):
        self.hashmap = {}
        

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        

    def get(self, key: int) -> int:
        return self.hashmap.get(key) if self.hashmap.get(key) is not None else -1
        

    def remove(self, key: int) -> None:
        if self.hashmap.get(key) is not None:
            self.hashmap.pop(key)
        
#general
#need to build a hashmap (no lib)

#init object with empty map
#create put to act as upsert
#make a get to return val or -1 if doesnt exist
#remove key value pairs when passed key

#constraints + edge cases
#remove called with nothing in? even then doesnt matter
#get either returns val or -1 
#put either adds new val or updates the key value pair

#tests + example

#english + pseudo 