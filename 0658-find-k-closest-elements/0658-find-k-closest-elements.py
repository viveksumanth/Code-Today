class Solution:
    def binarySearch(self, arr, left, right, target):
        closest = -1
        while(left <= right):
            mid = (left + right)//2
            if arr[mid] < target:
                closest = mid
                left = mid + 1
            else:
                right = mid - 1
        return closest

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        left = self.binarySearch(arr, 0, len(arr)-1, x)
        
        #sliding window
        right = left + 1

        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]

