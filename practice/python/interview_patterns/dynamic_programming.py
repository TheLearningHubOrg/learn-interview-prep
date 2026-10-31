"""Pattern 10: dynamic programming (state, transition, base case, order)."""


def climb_stairs(n: int) -> int:
    """Ways to climb n steps taking 1 or 2 at a time."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def coin_change(coins: list[int], amount: int) -> int:
    """Fewest coins summing to amount, or -1. Bottom-up, O(amount * coins)."""
    unreachable = amount + 1
    dp = [0] + [unreachable] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
    return -1 if dp[amount] == unreachable else dp[amount]


def house_robber(nums: list[int]) -> int:
    """Max sum of non-adjacent elements, in O(1) space."""
    skip, take = 0, 0
    for n in nums:
        skip, take = max(skip, take), skip + n
    return max(skip, take)


def longest_common_subsequence(a: str, b: str) -> int:
    """LCS length with two rolling rows. O(len(a) * len(b)) time."""
    prev = [0] * (len(b) + 1)
    for ch_a in a:
        cur = [0] * (len(b) + 1)
        for j, ch_b in enumerate(b, start=1):
            cur[j] = prev[j - 1] + 1 if ch_a == ch_b else max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]
