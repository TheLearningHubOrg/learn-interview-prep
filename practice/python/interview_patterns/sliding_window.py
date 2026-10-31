"""Pattern 3: sliding windows over contiguous ranges."""

from collections import Counter


def longest_unique_substring(s: str) -> int:
    """Length of the longest substring without repeated characters."""
    last_seen: dict[str, int] = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best


def max_sum_window(nums: list[int], k: int) -> int:
    """Maximum sum of any k consecutive elements (fixed-size window)."""
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


def min_window(s: str, t: str) -> str:
    """Smallest substring of s containing every character of t (with counts)."""
    if not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best_start, best_len = 0, len(s) + 1
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best_len > len(s) else s[best_start:best_start + best_len]
