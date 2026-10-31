"""Pattern 7: heaps for top-k, k-way merge and running order statistics."""

import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """The k most frequent values, most frequent first."""
    counts = Counter(nums)
    return [value for value, _ in heapq.nlargest(k, counts.items(), key=lambda kv: kv[1])]


def kth_largest(nums: list[int], k: int) -> int:
    """k-th largest element using a min-heap of size k. O(n log k)."""
    heap: list[int] = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists. O(N log k) where N is the total length."""
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    out: list[int] = []
    while heap:
        value, i, j = heapq.heappop(heap)
        out.append(value)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out
