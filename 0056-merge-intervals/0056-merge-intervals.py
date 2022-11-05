class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a,n=[],len(intervals)
        if n==1:
            return intervals
        intervals.sort()
        start,end=intervals[0][0],intervals[0][1]
        for i in range(1,n):
            s1,e1=intervals[i-1][0], intervals[i-1][1]
            s2,e2=intervals[i][0], intervals[i][1]
            if end>=s2:
                end=max(e2,end)
            else:
                a.append([start,end])
                start=s2
                end=max(e2,end)
        a.append([start,end])
        return a
        