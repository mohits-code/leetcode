class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        n = len(heights)
        m = len(heights[0])
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        q = deque()
        for i in range(n):
            q.append((i, 0))
        for j in range(1, m):
            q.append((0, j))

        while q:
            x, y = q.popleft()
            curr_val = heights[x][y]
            
            if curr_val < 0:
                continue
            
            original_h = curr_val
            heights[x][y] = -(original_h + 1)

            for dr, dc in dirs:
                nx, ny = x + dr, y + dc

                if 0 <= nx < n and 0 <= ny < m:
                    neighbor_val = heights[nx][ny]
                    neighbor_original_h = -neighbor_val - 1 if neighbor_val < 0 else neighbor_val
                    
                    if neighbor_original_h >= original_h:
                        q.append((nx, ny))
        
        res = set()
        visited = set()
        q = deque()
        for i in range(n):
            q.append((i, m - 1))
        for j in range(m - 1):
            q.append((n - 1, j))
        
        while q:
            x, y = q.popleft()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            curr_val = heights[x][y]
            
            if curr_val < 0:
                res.add((x, y))
            
            original_h = -curr_val - 1 if curr_val < 0 else curr_val
            
            for dr, dc in dirs:
                nx, ny = x + dr, y + dc

                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    neighbor_val = heights[nx][ny]
                    neighbor_original_h = -neighbor_val - 1 if neighbor_val < 0 else neighbor_val
                    
                    if neighbor_original_h >= original_h:
                        q.append((nx, ny))
        
        return list(res)