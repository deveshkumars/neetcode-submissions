class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        visitedBricks = defaultdict(int)

        

        wall_height = len(wall)
        wall_width = sum(wall[0])
        if len(wall[0]) == 1:
            return wall_height
        for layer in wall:
            x_coord = 0
            for brick in layer:
                # print(visitedBricks)
                x_coord += brick
                if x_coord != wall_width: visitedBricks[x_coord] += 1
        # print(visitedBricks)
        return wall_height - max(visitedBricks.values())
        return 0


#|##|##|#
###|#|##
#|###|##
##|####
###|#|##