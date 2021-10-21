class Solution:
    def search_binario(self, nums, target: int, start,end) -> int:
        if len(nums[start:end+1]) == 0:
            return -1
        else:
            indice_medio = (start + end ) // 2
            if target == nums[indice_medio]:
                return indice_medio
            elif target < nums[indice_medio]:
                return self.search_binario(nums, target, start, indice_medio - 1)
            else:
                return self.search_binario(nums, target, indice_medio+1, end)

    def search(self, nums, target: int) -> int:
        return self.search_binario(nums,target,0,len(nums)-1)


sol = Solution()
nums = [5]
respuesta = sol.search(nums, 5,0,len(nums)-1)
print(respuesta)
