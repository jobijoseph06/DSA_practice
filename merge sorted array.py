class Solution(object):
    def merge(self, nums1, m, nums2, n):
        total = m + n
        nums3 = [0] * total
        left = 0
        right = 0
        index = 0

        while left < m and right < n:
            if nums1[left] < nums2[right]:
                nums3[index] = nums1[left]
                index += 1
                left += 1
            else:
                nums3[index] = nums2[right]
                index += 1
                right += 1

        while left < m:
            nums3[index] = nums1[left]
            index += 1
            left += 1

        while right < n:
            nums3[index] = nums2[right]
            index += 1
            right += 1

        return nums3
obj = Solution()
print(obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3 ))