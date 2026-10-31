// Patterns 7, 11, 12 and 13: heaps, union-find, tries and LRU cache design.
// JavaScript has no built-in priority queue, so interviewers often expect you
// to write a small binary heap. This one takes a comparator.

export class MinHeap {
  #items = [];
  #less;

  constructor(less = (a, b) => a < b) {
    this.#less = less;
  }

  get size() {
    return this.#items.length;
  }

  peek() {
    return this.#items[0];
  }

  push(value) {
    const items = this.#items;
    items.push(value);
    let i = items.length - 1;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (!this.#less(items[i], items[parent])) break;
      [items[i], items[parent]] = [items[parent], items[i]];
      i = parent;
    }
  }

  pop() {
    const items = this.#items;
    if (items.length === 0) return undefined;
    const top = items[0];
    const last = items.pop();
    if (items.length > 0) {
      items[0] = last;
      let i = 0;
      for (;;) {
        const l = 2 * i + 1;
        const r = l + 1;
        let smallest = i;
        if (l < items.length && this.#less(items[l], items[smallest])) smallest = l;
        if (r < items.length && this.#less(items[r], items[smallest])) smallest = r;
        if (smallest === i) break;
        [items[i], items[smallest]] = [items[smallest], items[i]];
        i = smallest;
      }
    }
    return top;
  }
}

// ---------- Pattern 7: heaps and top-k ----------

export function kthLargest(nums, k) {
  const heap = new MinHeap();
  for (const n of nums) {
    heap.push(n);
    if (heap.size > k) heap.pop();
  }
  return heap.peek();
}

/** Bucket sort by frequency: O(n), no heap needed. Most frequent first. */
export function topKFrequent(nums, k) {
  const counts = new Map();
  for (const n of nums) counts.set(n, (counts.get(n) ?? 0) + 1);
  const buckets = Array.from({ length: nums.length + 1 }, () => []);
  for (const [value, count] of counts) buckets[count].push(value);
  const out = [];
  for (let c = buckets.length - 1; c >= 0 && out.length < k; c--) {
    for (const value of buckets[c]) {
      out.push(value);
      if (out.length === k) break;
    }
  }
  return out;
}

export function mergeKSorted(lists) {
  const heap = new MinHeap((a, b) => a[0] < b[0]);
  lists.forEach((list, i) => {
    if (list.length) heap.push([list[0], i, 0]);
  });
  const out = [];
  while (heap.size) {
    const [value, i, j] = heap.pop();
    out.push(value);
    if (j + 1 < lists[i].length) heap.push([lists[i][j + 1], i, j + 1]);
  }
  return out;
}

// ---------- Pattern 11: union-find ----------

export class UnionFind {
  constructor(size) {
    this.parent = Array.from({ length: size }, (_, i) => i);
    this.rank = new Array(size).fill(0);
    this.components = size;
  }

  find(x) {
    while (this.parent[x] !== x) {
      this.parent[x] = this.parent[this.parent[x]];
      x = this.parent[x];
    }
    return x;
  }

  union(a, b) {
    let ra = this.find(a);
    let rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    this.components--;
    return true;
  }
}

export function countComponents(n, edges) {
  const uf = new UnionFind(n);
  for (const [a, b] of edges) uf.union(a, b);
  return uf.components;
}

// ---------- Pattern 12: trie ----------

export class Trie {
  constructor() {
    this.root = { children: new Map(), isWord: false };
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node.children.has(ch)) node.children.set(ch, { children: new Map(), isWord: false });
      node = node.children.get(ch);
    }
    node.isWord = true;
  }

  #walk(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      node = node.children.get(ch);
      if (!node) return null;
    }
    return node;
  }

  search(word) {
    return this.#walk(word)?.isWord === true;
  }

  startsWith(prefix) {
    return this.#walk(prefix) !== null;
  }
}

// ---------- Pattern 13: LRU cache (Map keeps insertion order) ----------

export class LRUCache {
  #map = new Map();

  constructor(capacity) {
    if (!(capacity > 0)) throw new RangeError('capacity must be positive');
    this.capacity = capacity;
  }

  get(key) {
    if (!this.#map.has(key)) return undefined;
    const value = this.#map.get(key);
    this.#map.delete(key); // re-insert to mark as most recently used
    this.#map.set(key, value);
    return value;
  }

  put(key, value) {
    this.#map.delete(key);
    this.#map.set(key, value);
    if (this.#map.size > this.capacity) {
      const oldest = this.#map.keys().next().value;
      this.#map.delete(oldest);
    }
  }

  get size() {
    return this.#map.size;
  }
}
