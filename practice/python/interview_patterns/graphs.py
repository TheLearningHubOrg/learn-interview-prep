"""Pattern 8: BFS/DFS on grids and graphs, plus topological sort."""

from collections import deque

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def num_islands(grid: list[str]) -> int:
    """Count 4-connected groups of '1' cells. Does not mutate the input."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen: set[tuple[int, int]] = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            queue = deque([(r, c)])
            seen.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
    return islands


def course_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Kahn's algorithm. Pairs are [course, prerequisite]. [] if there is a cycle."""
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order: list[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == num_courses else []


def shortest_path_grid(grid: list[str]) -> int:
    """Fewest steps from top-left to bottom-right through '.' cells, or -1."""
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] != "." or grid[rows - 1][cols - 1] != ".":
        return -1
    queue = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "." and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1
