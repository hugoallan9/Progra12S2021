class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            pivot_index = (left + right) // 2
            pivote = nums[pivot_index]
            if pivote == target:
                return pivot_index
            elif target > pivote:
                left = pivot_index + 1
            elif target < pivote:
                right = pivot_index - 1
        return -1




sol = Solution()
nums = [-1,0,3,5,9,12]
respuesta = sol.search(nums, 12)
print(respuesta)