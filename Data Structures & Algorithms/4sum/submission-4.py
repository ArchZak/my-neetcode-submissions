class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #input: array of nums + target number
        #output: array of arrays of all values that add up to target

        #the indices need to be distinct

        #threesum is a for loop + two pointer
        #foursum is gonna be a two pointer + another two pointer
        #gonna sort first
        #we move inner two pointer to try and get closer to answer
        #same with outer

        nums.sort()
        #gonna track answers by having a hashmap with sorted tuple key : whatever array answer
        tracker = {}

        for left1 in range(len(nums)//2): # goes right
            for right1 in range(len(nums)-1, (len(nums)-1)//2, -1): # goes 
                left2, right2 = 0, len(nums)-1
                while left2 < right2:
                    # dont want dupe indexes
                    # has to equal target
                    if left1 == left2 or right1 == left2:
                        left2+=1
                        continue
                    elif right1 == right2 or left1 == right2:
                        right2-=1
                        continue

                    if nums[left1]+nums[right1]+nums[left2]+nums[right2] > target:
                        right2-=1
                    elif nums[left1]+nums[right1]+nums[left2]+nums[right2] < target:
                        left2+=1
                    else:
                        value = sorted([nums[left1],nums[right1],nums[left2],nums[right2]])
                        key = tuple(value)
                        tracker[key] = value
                        left2+=1
                        right2-=1

        return list(tracker.values())