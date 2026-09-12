class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # xyxxyzbzbbisl
        # x: 0:3
        # y: 1:4
        # z: 5:5
        # b: 6:9
        # z: 5:7
        # i: 10
        # s: 11
        # l: 12

        last_instances = {}
        for i in range(len(s)):
            last_instances[s[i]] = i
        # print(last_instances)
        beginning_of_current = 0
        end_of_current = 0
        lens = []
        for i in range(len(s)):
            end_of_current = max(end_of_current, last_instances[s[i]])
            if i == end_of_current:
                lens.append(end_of_current - beginning_of_current + 1)
                beginning_of_current = i + 1
        return lens


        
