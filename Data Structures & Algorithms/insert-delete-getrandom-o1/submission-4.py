class RandomizedSet:

    def __init__(self):
        self.hashdict = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        #check dict first, if in set, return false
        #if not in set, add to list, then add key value pair + return true

        if val not in self.hashdict:
            self.array.append(val)
            self.hashdict[val] = len(self.array)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        #check dict first, if not in set, return false
        #if in set, check the index, make sure it's last, then pop from both + true
        #need to swap curr index with last index
        #if last index alr, just continue swap is just wasting

        if val in self.hashdict:
            #index of value we're interested in taking out
            val_index = self.hashdict[val]
            #value of num curr last
            last = self.array[-1]
            #update index of last to new
            self.hashdict[last] = val_index
            #swap last to val_index
            self.array[val_index] = last
            

            self.array.pop()
            self.hashdict.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        #generate a number within the range of the len of the list and return it
        return self.array[random.randrange(len(self.array))]
        
        
        
#general

#init randomized set object for the whole class
#insert inserts an item val into the set if not present, true if not present false otw
#remove removes an item val from the set if present, true if was present false otw
#return a random element from the current set of elements (will have at least one in set)
#each element must have the same probability of being returned 

#constraints + edge cases
#each function works in average o(1) time complexity 
#get random wont be called on an empty set
#wont have to deal with duplicates

#tests + examples


#english + pseudo: 
#need to use a list for constant random indexing and dict for constant add and remove

#so going to init a hash dict + normal list

#going to use dict with key-value : input:index
#this lets append to array, and put index + val in the dict in constant time 
#this lets us swap val of choice to end of array and remove from dict+list in constant time
#then get random is easy bc we just pull random index in range of len