"""Pattern 4: binary search over sorted data and over answer spaces."""


def lower_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] >= target (len(nums) if none)."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated(nums: list[int], target: int) -> int:
    """Index of target in a rotated sorted array of distinct values, or -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def min_ship_capacity(weights: list[int], days: int) -> int:
    """Smallest capacity that ships all packages, in order, within `days`.

    Binary search on the answer: feasibility is monotonic in capacity.
    """
    def fits(capacity: int) -> bool:
        used_days, load = 1, 0
        for w in weights:
            if load + w > capacity:
                used_days += 1
                load = 0
            load += w
        return used_days <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if fits(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
