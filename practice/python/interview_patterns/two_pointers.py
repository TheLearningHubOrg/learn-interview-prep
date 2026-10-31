"""Pattern 2: two pointers moving towards each other over a sequence."""


def is_palindrome(s: str) -> bool:
    """True if s reads the same both ways, ignoring case and non-alphanumerics."""
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets that sum to zero. Sort, then two-pointer per anchor.

    Time O(n^2), extra space O(1) beyond the output (sorting aside).
    """
    nums = sorted(nums)
    result: list[list[int]] = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result


def max_water_container(heights: list[int]) -> int:
    """Largest area between two lines; always move the shorter side inwards."""
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
