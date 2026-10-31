"""Pattern 5: sort intervals by start, then sweep."""

import heapq


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping [start, end] intervals."""
    merged: list[list[int]] = []
    for start, end in sorted(intervals, key=lambda iv: iv[0]):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Minimum rooms so that no two overlapping meetings share one.

    A min-heap holds end times of meetings currently in progress.
    """
    ends: list[int] = []
    for start, end in sorted(intervals, key=lambda iv: iv[0]):
        if ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
    return len(ends)
