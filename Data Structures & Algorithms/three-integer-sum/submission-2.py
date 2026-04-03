class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]

        for index, num in enumerate(nums):
            left,right=0,len(nums)-1
            while left < right:
                if nums[left]+nums[right]+num>0:
                    right-=1
                elif nums[left]+nums[right]+num<0:
                    left+=1
                else:
                    triplet = [nums[left],nums[right],num]
                    triplet.sort()
                    if left != index and right != index and triplet not in answer:
                        answer.append(triplet)
                    right-=1
                    left+=1

        return answer
