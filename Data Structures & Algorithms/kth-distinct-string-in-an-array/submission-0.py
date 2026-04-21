class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        #input: array of characters, and int k
        #output: the  kth distinct string in the array or "" if fewer than kth distinct strings

        tracker = {}
        counter = 0
        for letter in arr:
            tracker[letter] = tracker.get(letter, 0) + 1

        answer = []
        for key, value in tracker.items():
            if value == 1:
                answer.append(key)

        if k > len(answer):
            return ""

        return answer[k-1]
        