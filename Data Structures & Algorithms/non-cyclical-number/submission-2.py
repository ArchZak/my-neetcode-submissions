class Solution:
    def isHappy(self, n: int) -> bool:
        #non cyclical num is:
        #given + int, replace it with sum of squares of its digits
        #repeat above step until the number = 1 or a number we've already seen

        #going to have a tracking set to check if we've seen a number yet
        #loop through a num by converting to string and then reconverting to int
        #square each number, add them, check if it's 1 or in the set
        #if 1 then return true
        #if in set exit and return false

        tracker = set([n])

        answer = 0
        curr_num = n

        while answer != 1 and curr_num != 1:
            answer = 0
            string_n = str(curr_num)
            for i in range(len(string_n)):
                answer += int(string_n[i])**2
            
            if answer in tracker:
                return False
            else:
                tracker.add(answer)
                curr_num = answer

        return True
