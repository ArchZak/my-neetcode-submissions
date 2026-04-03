class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i, num in enumerate(nums):
            left, right = 0, len(nums)-1
            while left < right:
                if nums[left]+nums[right]+nums[i] > 0:
                    right-=1
                elif nums[left]+nums[right]+nums[i] < 0:
                    left+=1
                else:
                    ans = sorted([nums[left],nums[right],nums[i]])
                    if ans not in answer and left != i and right != i:
                        answer.append(ans)
                    left+=1
                    right-=1

        return answer