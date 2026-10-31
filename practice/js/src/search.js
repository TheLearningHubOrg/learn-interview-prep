// Patterns 8-10: graph traversal, backtracking and dynamic programming.

const DIRECTIONS = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

// ---------- Pattern 8: BFS / DFS / topological sort ----------

/** Count 4-connected islands of '1'. Uses an index-based queue (Array#shift is O(n)). */
export function numIslands(grid) {
  if (grid.length === 0) return 0;
  const rows = grid.length;
  const cols = grid[0].length;
  const seen = new Set();
  const key = (r, c) => r * cols + c;
  let islands = 0;
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] !== '1' || seen.has(key(r, c))) continue;
      islands++;
      const queue = [[r, c]];
      seen.add(key(r, c));
      for (let head = 0; head < queue.length; head++) {
        const [cr, cc] = queue[head];
        for (const [dr, dc] of DIRECTIONS) {
          const nr = cr + dr;
          const nc = cc + dc;
          if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
          if (grid[nr][nc] !== '1' || seen.has(key(nr, nc))) continue;
          seen.add(key(nr, nc));
          queue.push([nr, nc]);
        }
      }
    }
  }
  return islands;
}

/** Kahn's algorithm. Pairs are [course, prerequisite]; returns [] on a cycle. */
export function courseOrder(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const indegree = new Array(numCourses).fill(0);
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    indegree[course]++;
  }
  const queue = [];
  indegree.forEach((d, i) => d === 0 && queue.push(i));
  const order = [];
  for (let head = 0; head < queue.length; head++) {
    const node = queue[head];
    order.push(node);
    for (const next of graph[node]) {
      if (--indegree[next] === 0) queue.push(next);
    }
  }
  return order.length === numCourses ? order : [];
}

// ---------- Pattern 9: backtracking ----------

export function subsets(nums) {
  const result = [];
  const path = [];
  const explore = (start) => {
    result.push([...path]);
    for (let i = start; i < nums.length; i++) {
      path.push(nums[i]);
      explore(i + 1);
      path.pop();
    }
  };
  explore(0);
  return result;
}

export function permutations(nums) {
  const result = [];
  const path = [];
  const used = new Array(nums.length).fill(false);
  const explore = () => {
    if (path.length === nums.length) {
      result.push([...path]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(nums[i]);
      explore();
      path.pop();
      used[i] = false;
    }
  };
  explore();
  return result;
}

// ---------- Pattern 10: dynamic programming ----------

export function climbStairs(n) {
  let [a, b] = [1, 1];
  for (let i = 0; i < n; i++) [a, b] = [b, a + b];
  return a;
}

export function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let a = 1; a <= amount; a++) {
    for (const coin of coins) {
      if (coin <= a) dp[a] = Math.min(dp[a], dp[a - coin] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}

export function longestCommonSubsequence(a, b) {
  let prev = new Array(b.length + 1).fill(0);
  for (const chA of a) {
    const cur = new Array(b.length + 1).fill(0);
    for (let j = 1; j <= b.length; j++) {
      cur[j] = chA === b[j - 1] ? prev[j - 1] + 1 : Math.max(prev[j], cur[j - 1]);
    }
    prev = cur;
  }
  return prev[b.length];
}

/** Top-down variant with memoisation, to compare with the bottom-up form above. */
export function uniquePaths(rows, cols, memo = new Map()) {
  if (rows === 1 || cols === 1) return 1;
  const key = `${rows},${cols}`;
  if (!memo.has(key)) {
    memo.set(key, uniquePaths(rows - 1, cols, memo) + uniquePaths(rows, cols - 1, memo));
  }
  return memo.get(key);
}
