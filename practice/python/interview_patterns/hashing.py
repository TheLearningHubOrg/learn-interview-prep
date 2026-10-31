"""Pattern 1: hash maps for O(1) lookups and grouping."""

from collections import defaultdict


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices (i, j), i < j, with nums[i] + nums[j] == target.

    One pass: for each value, ask whether its complement was seen earlier.
    Time O(n), space O(n).
    """
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in seen:
            return seen[need], i
        seen[value] = i
    return None


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other, keeping input order.

    The sorted letters form a canonical key. Time O(n * k log k).
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


def first_unique_char(s: str) -> int:
    """Index of the first character that appears exactly once, or -1."""
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
