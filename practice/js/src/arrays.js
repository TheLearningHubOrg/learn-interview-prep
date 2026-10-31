// Patterns 1-6: hashing, two pointers, sliding window, binary search,
// intervals and monotonic stacks. Each export mirrors the Python solution
// with the same name (snake_case there, camelCase here).

// ---------- Pattern 1: hash maps ----------

/** Indices [i, j] with nums[i] + nums[j] === target, or null. O(n). */
export function twoSum(nums, target) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (seen.has(need)) return [seen.get(need), i];
    seen.set(nums[i], i);
  }
  return null;
}

/** Groups of anagrams, keyed by their sorted letters. */
export function groupAnagrams(words) {
  const groups = new Map();
  for (const word of words) {
    const key = [...word].sort().join('');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(word);
  }
  return [...groups.values()];
}

// ---------- Pattern 2: two pointers ----------

const isAlnum = (ch) => /[a-z0-9]/i.test(ch);

export function isPalindrome(s) {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    if (!isAlnum(s[left])) left++;
    else if (!isAlnum(s[right])) right--;
    else if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
    else {
      left++;
      right--;
    }
  }
  return true;
}

/** Unique zero-sum triplets. Note the numeric comparator: sort() is lexicographic by default. */
export function threeSum(input) {
  const nums = [...input].sort((a, b) => a - b);
  const result = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const total = nums[i] + nums[left] + nums[right];
      if (total < 0) left++;
      else if (total > 0) right--;
      else {
        result.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
        while (left < right && nums[left] === nums[left - 1]) left++;
      }
    }
  }
  return result;
}

// ---------- Pattern 3: sliding window ----------

export function longestUniqueSubstring(s) {
  const lastSeen = new Map();
  let start = 0;
  let best = 0;
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (lastSeen.has(ch) && lastSeen.get(ch) >= start) start = lastSeen.get(ch) + 1;
    lastSeen.set(ch, i);
    best = Math.max(best, i - start + 1);
  }
  return best;
}

export function minWindow(s, t) {
  if (t.length === 0) return '';
  const need = new Map();
  for (const ch of t) need.set(ch, (need.get(ch) ?? 0) + 1);
  let missing = t.length;
  let left = 0;
  let bestStart = 0;
  let bestLen = Infinity;
  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    if ((need.get(ch) ?? 0) > 0) missing--;
    need.set(ch, (need.get(ch) ?? 0) - 1);
    while (missing === 0) {
      if (right - left + 1 < bestLen) {
        bestStart = left;
        bestLen = right - left + 1;
      }
      const out = s[left];
      need.set(out, need.get(out) + 1);
      if (need.get(out) > 0) missing++;
      left++;
    }
  }
  return bestLen === Infinity ? '' : s.slice(bestStart, bestStart + bestLen);
}

// ---------- Pattern 4: binary search ----------

/** First index with nums[i] >= target. */
export function lowerBound(nums, target) {
  let lo = 0;
  let hi = nums.length;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (nums[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

export function searchRotated(nums, target) {
  let lo = 0;
  let hi = nums.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    if (nums[mid] === target) return mid;
    if (nums[lo] <= nums[mid]) {
      if (nums[lo] <= target && target < nums[mid]) hi = mid - 1;
      else lo = mid + 1;
    } else if (nums[mid] < target && target <= nums[hi]) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}

/** Binary search on the answer: the smallest capacity that ships in `days`. */
export function minShipCapacity(weights, days) {
  const fits = (capacity) => {
    let used = 1;
    let load = 0;
    for (const w of weights) {
      if (load + w > capacity) {
        used++;
        load = 0;
      }
      load += w;
    }
    return used <= days;
  };
  let lo = Math.max(...weights);
  let hi = weights.reduce((a, b) => a + b, 0);
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (fits(mid)) hi = mid;
    else lo = mid + 1;
  }
  return lo;
}

// ---------- Pattern 5: intervals ----------

export function mergeIntervals(intervals) {
  const sorted = intervals.map(([s, e]) => [s, e]).sort((a, b) => a[0] - b[0]);
  const merged = [];
  for (const [start, end] of sorted) {
    const last = merged.at(-1);
    if (last && start <= last[1]) last[1] = Math.max(last[1], end);
    else merged.push([start, end]);
  }
  return merged;
}

/** Sweep line: +1 at each start, -1 at each end; ends sort before starts at the same time. */
export function minMeetingRooms(intervals) {
  const events = [];
  for (const [s, e] of intervals) events.push([s, 1], [e, -1]);
  events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  let rooms = 0;
  let peak = 0;
  for (const [, delta] of events) {
    rooms += delta;
    peak = Math.max(peak, rooms);
  }
  return peak;
}

// ---------- Pattern 6: monotonic stack ----------

export function dailyTemperatures(temps) {
  const answer = new Array(temps.length).fill(0);
  const stack = [];
  temps.forEach((t, i) => {
    while (stack.length && temps[stack.at(-1)] < t) {
      const j = stack.pop();
      answer[j] = i - j;
    }
    stack.push(i);
  });
  return answer;
}
