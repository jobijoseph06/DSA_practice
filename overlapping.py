def overlapping(arr):
   og = []
   arr.sort()
   for interval in arr:
       if not og or og[-1][1] < interval[0]:
           og.append(interval)
       else:
           og[-1][1] = max(og[-1][1], interval[1])
           og[-1][0] = min(og[-1][0], interval[0])
   return og

print(overlapping([[1,4],[0,0]]))