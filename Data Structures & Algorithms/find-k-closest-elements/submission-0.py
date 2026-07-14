class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #input: a sorted array of ints, and two ints k(k closest ints), x(target num)
        #output: sorted array of k ints closest to x

        #a is closer to x than b:
        # |a-x| < |b-x| or |a-x|==|b-x| and a<b

        #going to make a window of size k
        #going to loop through array with window
        #gonna do abs(a-x) of each num in window, lowest sum wins

        answer, total = None, 99999
        for i in range(len(arr)-k+1):
            temp = 0
            for num in arr[i:i+k]:
                temp+=abs(num-x)
            if temp < total:
                total = temp
                answer = arr[i:i+k]
        
        return answer