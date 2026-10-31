"""Pattern 9: backtracking (choose, explore, un-choose)."""


def subsets(nums: list[int]) -> list[list[int]]:
    """Every subset of distinct nums. 2^n results."""
    result: list[list[int]] = []
    path: list[int] = []

    def explore(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            explore(i + 1)
            path.pop()

    explore(0)
    return result


def permutations(nums: list[int]) -> list[list[int]]:
    """Every ordering of distinct nums. n! results."""
    result: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def explore() -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i, value in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(value)
            explore()
            path.pop()
            used[i] = False

    explore()
    return result


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Combinations (values reusable) summing to target, without duplicates."""
    candidates = sorted(candidates)
    result: list[list[int]] = []
    path: list[int] = []

    def explore(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # sorted, so every later candidate is too big as well
            path.append(candidates[i])
            explore(i, remaining - candidates[i])
            path.pop()

    explore(0, target)
    return result
