def repeating(nums):
   freq = []
   n = len(nums)
   for i in range(n):
       freq.append(0)

   for i in range(n):
       num = nums[i]
       freq[num-1] +=1
   print(freq)

   repeat = 0
   missing = 0
   for i in range(n):
       if freq[i] == 2:
           repeat = i+1
       if freq[i] == 0:
           missing = i+1
   return [repeat, missing]
print(repeating([1, 2, 3, 6, 7, 5, 7]))
