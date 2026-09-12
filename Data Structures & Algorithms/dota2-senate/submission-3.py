class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_cancels, r_cancels = 0, 0
        queue = deque()
        for char in senate: queue.append(char)
        while len(queue) > 1 and len(set(list(queue))) == 2:
            # print(f"queue: {queue}")
            char = queue.popleft()
            if char == "R":
                if r_cancels > 0:
                    r_cancels -= 1
                    continue
                else:
                    d_cancels += 1
                    queue.append("R")
            elif char == "D":
                if d_cancels > 0:
                    d_cancels -= 1
                    continue
                else:
                    r_cancels += 1
                    queue.append("D")
        return "Radiant" if queue[0] == "R" else "Dire"
