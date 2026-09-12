class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        visitedBricks = defaultdict(int)

        wall_height = len(wall)
        wall_width = sum(wall[0])

        for layer in wall:
            x_coord = 0
            for brick in layer:
                # print(visitedBricks)
                x_coord += brick
                visitedBricks[x_coord] += 1
        print(visitedBricks)
        visitedBricks[wall_width] = 0
        return wall_height - max(visitedBricks.values())