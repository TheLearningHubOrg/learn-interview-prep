"""Pattern 6: monotonic stacks for "next greater / smaller" questions."""


def daily_temperatures(temps: list[int]) -> list[int]:
    """Days to wait for a warmer temperature (0 if never)."""
    answer = [0] * len(temps)
    stack: list[int] = []  # indices with strictly decreasing temperatures
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


def largest_rectangle(heights: list[int]) -> int:
    """Largest rectangle in a histogram, using a sentinel bar of height 0."""
    bars = heights + [0]
    stack: list[int] = []
    best = 0
    for i, h in enumerate(bars):
        while stack and bars[stack[-1]] >= h:
            height = bars[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best
