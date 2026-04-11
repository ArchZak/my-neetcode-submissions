class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #input: int array of nums
        #output: return all the values that add up the 0 where theyre all distinct
        #not duplicate triplets, return output and triplets in any order

        #want to sort the input
        #after sorting the input, do a for loop to pick a num and init l and r
        #do two pointer solution to find the occurrences of 0
        #put inputs as sorted values into set to avoid dupes


        nums.sort()
        tracker=[]

        for i in range(len(nums)):
            l, r = 0, len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp > 0:
                    r-=1
                elif temp < 0:
                    l+=1
                else:
                    triplet = sorted([nums[i], nums[l], nums[r]])
                    if l != i and r!= i and triplet not in tracker:
                        tracker.append(triplet)
                    r-=1
                    l+=1

        return tracker

        