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
   duplicate = 0
   for i in range(n):
       if freq[i] == 2:
           repeat = i+1
       if freq[i] == 0:
           duplicate = i+1
   return [repeat, duplicate]
print(repeating([3, 5, 4, 1, 1]))
