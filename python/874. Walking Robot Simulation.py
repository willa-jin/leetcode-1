class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        假定往北direction = 0，此时向右转，转为向东，direction = 1，再向右转，direction = 2，
        转为向南，再右转，direction = 3，方向向西。如果再往右转，direction = 0，
        回到往北的方向。故向右转时，有规律direction = (direction + 1) % 4。
        可以用set集合把障碍物坐标存下来，一旦遇到障碍物，就停下来，等着接收下一条指令。
        每接收一次指令，检查一下当前坐标与原点的距离，看能否更新最大值。
        """
        obstacles = set(map(tuple, obstacles))
        move = [(0,1), (1, 0), (0, -1), (-1,0)]
        
        i = j = maxDis = d = 0
        
        for c in commands:
              if c == -1: 
                  d = (d + 1) % 4
              elif c == -2:
                  d = (d - 1) % 4
              else:
                   d_x, d_y = move[d]
                   for _ in range(c):
                       if (i + d_x, j + d_y) not in obstacles:
                           i += d_x
                           j += d_y
              maxDis = max(maxDis, i**2 + j**2)
         
         return maxDis
        
        
        
        
