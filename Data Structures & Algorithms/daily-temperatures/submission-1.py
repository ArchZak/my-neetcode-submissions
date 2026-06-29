class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
            count = -1
            for j in range(i, len(temperatures)):
                count+=1
                if temperatures[i] < temperatures[j]:
                    answer[i] = count
                    break
        
        return answer
