import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

import {
  twoSum,
  groupAnagrams,
  isPalindrome,
  threeSum,
  longestUniqueSubstring,
  minWindow,
  lowerBound,
  searchRotated,
  minShipCapacity,
  mergeIntervals,
  minMeetingRooms,
  dailyTemperatures,
} from '../src/arrays.js';
import {
  MinHeap,
  kthLargest,
  topKFrequent,
  mergeKSorted,
  countComponents,
  Trie,
  LRUCache,
} from '../src/structures.js';
import {
  numIslands,
  courseOrder,
  subsets,
  permutations,
  climbStairs,
  coinChange,
  longestCommonSubsequence,
  uniquePaths,
} from '../src/search.js';

const sortGroups = (groups) => groups.map((g) => [...g].sort()).sort();

describe('hashing', () => {
  it('twoSum finds the pair or returns null', () => {
    assert.deepEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
    assert.deepEqual(twoSum([3, 3], 6), [0, 1]);
    assert.equal(twoSum([1, 2, 3], 100), null);
  });

  it('groupAnagrams groups by sorted letters', () => {
    assert.deepEqual(
      sortGroups(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])),
      [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']],
    );
  });
});

describe('two pointers', () => {
  it('isPalindrome ignores case and punctuation', () => {
    assert.equal(isPalindrome('A man, a plan, a canal: Panama'), true);
    assert.equal(isPalindrome('race a car'), false);
    assert.equal(isPalindrome(''), true);
  });

  it('threeSum returns unique triplets and sorts numerically', () => {
    assert.deepEqual(threeSum([-1, 0, 1, 2, -1, -4]), [
      [-1, -1, 2],
      [-1, 0, 1],
    ]);
    assert.deepEqual(threeSum([-10, 5, 5, 0]), [[-10, 5, 5]]);
    assert.deepEqual(threeSum([0, 0, 0, 0]), [[0, 0, 0]]);
  });
});

describe('sliding window', () => {
  it('longestUniqueSubstring', () => {
    for (const [s, n] of [['abcabcbb', 3], ['bbbbb', 1], ['pwwkew', 3], ['', 0], ['abba', 2]]) {
      assert.equal(longestUniqueSubstring(s), n, s);
    }
  });

  it('minWindow', () => {
    assert.equal(minWindow('ADOBECODEBANC', 'ABC'), 'BANC');
    assert.equal(minWindow('a', 'aa'), '');
    assert.equal(minWindow('aa', 'aa'), 'aa');
  });
});

describe('binary search', () => {
  it('lowerBound', () => {
    assert.equal(lowerBound([1, 2, 4, 4, 5], 4), 2);
    assert.equal(lowerBound([1, 2, 3], 10), 3);
    assert.equal(lowerBound([], 1), 0);
  });

  it('searchRotated finds every element', () => {
    const nums = [4, 5, 6, 7, 0, 1, 2];
    nums.forEach((v, i) => assert.equal(searchRotated(nums, v), i));
    assert.equal(searchRotated(nums, 3), -1);
  });

  it('minShipCapacity searches the answer space', () => {
    assert.equal(minShipCapacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15);
    assert.equal(minShipCapacity([3, 2, 2, 4, 1, 4], 3), 6);
  });
});

describe('intervals and monotonic stack', () => {
  it('mergeIntervals does not mutate input', () => {
    const input = [[2, 6], [1, 3], [8, 10]];
    assert.deepEqual(mergeIntervals(input), [[1, 6], [8, 10]]);
    assert.deepEqual(input, [[2, 6], [1, 3], [8, 10]]);
    assert.deepEqual(mergeIntervals([[1, 4], [4, 5]]), [[1, 5]]);
  });

  it('minMeetingRooms treats back-to-back meetings as non-overlapping', () => {
    assert.equal(minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2);
    assert.equal(minMeetingRooms([[1, 5], [5, 10]]), 1);
    assert.equal(minMeetingRooms([]), 0);
  });

  it('dailyTemperatures', () => {
    assert.deepEqual(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0]);
  });
});

describe('heaps', () => {
  it('MinHeap pops in ascending order', () => {
    const heap = new MinHeap();
    [5, 3, 8, 1, 9, 2].forEach((n) => heap.push(n));
    const out = [];
    while (heap.size) out.push(heap.pop());
    assert.deepEqual(out, [1, 2, 3, 5, 8, 9]);
    assert.equal(heap.pop(), undefined);
  });

  it('kthLargest, topKFrequent, mergeKSorted', () => {
    assert.equal(kthLargest([3, 2, 1, 5, 6, 4], 2), 5);
    assert.deepEqual(topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2]);
    assert.deepEqual(mergeKSorted([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6]);
    assert.deepEqual(mergeKSorted([[], []]), []);
  });
});

describe('graphs', () => {
  it('numIslands', () => {
    assert.equal(numIslands(['11000', '11000', '00100', '00011']), 3);
    assert.equal(numIslands([]), 0);
  });

  it('courseOrder respects prerequisites and detects cycles', () => {
    const order = courseOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]);
    const pos = new Map(order.map((c, i) => [c, i]));
    assert.equal(order.length, 4);
    assert.ok(pos.get(0) < pos.get(1) && pos.get(1) < pos.get(3));
    assert.ok(pos.get(0) < pos.get(2) && pos.get(2) < pos.get(3));
    assert.deepEqual(courseOrder(2, [[1, 0], [0, 1]]), []);
  });
});

describe('backtracking', () => {
  it('subsets and permutations have the right sizes', () => {
    assert.equal(subsets([1, 2, 3]).length, 8);
    const perms = permutations([1, 2, 3]);
    assert.equal(perms.length, 6);
    assert.equal(new Set(perms.map((p) => p.join(','))).size, 6);
  });
});

describe('dynamic programming', () => {
  it('climbStairs', () => {
    assert.deepEqual([0, 1, 2, 3, 5, 10].map(climbStairs), [1, 1, 2, 3, 8, 89]);
  });

  it('coinChange beats greedy', () => {
    assert.equal(coinChange([1, 2, 5], 11), 3);
    assert.equal(coinChange([2], 3), -1);
    assert.equal(coinChange([1, 3, 4], 6), 2);
  });

  it('longestCommonSubsequence and uniquePaths', () => {
    assert.equal(longestCommonSubsequence('abcde', 'ace'), 3);
    assert.equal(uniquePaths(3, 7), 28);
  });
});

describe('union-find, trie, LRU cache', () => {
  it('countComponents', () => {
    assert.equal(countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2);
  });

  it('Trie', () => {
    const trie = new Trie();
    ['apple', 'app'].forEach((w) => trie.insert(w));
    assert.equal(trie.search('app'), true);
    assert.equal(trie.search('ap'), false);
    assert.equal(trie.startsWith('ap'), true);
    assert.equal(trie.startsWith('b'), false);
  });

  it('LRUCache evicts the least recently used key', () => {
    const cache = new LRUCache(2);
    cache.put(1, 'one');
    cache.put(2, 'two');
    assert.equal(cache.get(1), 'one');
    cache.put(3, 'three');
    assert.equal(cache.get(2), undefined);
    assert.equal(cache.get(3), 'three');
    assert.equal(cache.size, 2);
    assert.throws(() => new LRUCache(0), RangeError);
  });
});
