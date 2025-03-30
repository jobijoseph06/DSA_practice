def overlapping(arr):
   og = []
   for interval in arr:
       if not og or og[-1][1] < interval[0]:
           og.append(interval)
       else:
           og[-1][1] = max(og[-1][1], interval[1])
   return og

print(overlapping([[1,3],[2,6],[8,10],[15,18]]))