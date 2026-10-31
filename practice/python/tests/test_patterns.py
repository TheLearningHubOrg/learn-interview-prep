"""One test module per guide: every solved problem, including edge cases."""

import pytest

from interview_patterns.backtracking import combination_sum, permutations, subsets
from interview_patterns.binary_search import lower_bound, min_ship_capacity, search_rotated
from interview_patterns.dynamic_programming import (
    climb_stairs,
    coin_change,
    house_robber,
    longest_common_subsequence,
)
from interview_patterns.graphs import course_order, num_islands, shortest_path_grid
from interview_patterns.hashing import first_unique_char, group_anagrams, two_sum
from interview_patterns.heaps import kth_largest, merge_k_sorted, top_k_frequent
from interview_patterns.intervals import merge_intervals, min_meeting_rooms
from interview_patterns.lru_cache import LRUCache
from interview_patterns.monotonic_stack import daily_temperatures, largest_rectangle
from interview_patterns.sliding_window import (
    longest_unique_substring,
    max_sum_window,
    min_window,
)
from interview_patterns.trie import Trie
from interview_patterns.two_pointers import is_palindrome, max_water_container, three_sum
from interview_patterns.union_find import count_components, redundant_connection


class TestHashing:
    def test_two_sum_finds_pair(self):
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)
        assert two_sum([3, 2, 4], 6) == (1, 2)

    def test_two_sum_duplicates_and_missing(self):
        assert two_sum([3, 3], 6) == (0, 1)
        assert two_sum([1, 2, 3], 100) is None
        assert two_sum([], 0) is None

    def test_group_anagrams(self):
        groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert sorted(sorted(g) for g in groups) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    def test_first_unique_char(self):
        assert first_unique_char("leetcode") == 0
        assert first_unique_char("loveleetcode") == 2
        assert first_unique_char("aabb") == -1


class TestTwoPointers:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [("A man, a plan, a canal: Panama", True), ("race a car", False), ("", True), (".,", True)],
    )
    def test_is_palindrome(self, text, expected):
        assert is_palindrome(text) is expected

    def test_three_sum_unique_triplets(self):
        assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
        assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
        assert three_sum([1, 2]) == []

    def test_max_water_container(self):
        assert max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        assert max_water_container([1, 1]) == 1


class TestSlidingWindow:
    @pytest.mark.parametrize(
        ("text", "expected"), [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("abba", 2)]
    )
    def test_longest_unique_substring(self, text, expected):
        assert longest_unique_substring(text) == expected

    def test_max_sum_window(self):
        assert max_sum_window([2, 1, 5, 1, 3, 2], 3) == 9
        assert max_sum_window([-3, -1, -2], 1) == -1
        with pytest.raises(ValueError):
            max_sum_window([1, 2], 3)

    def test_min_window(self):
        assert min_window("ADOBECODEBANC", "ABC") == "BANC"
        assert min_window("a", "aa") == ""
        assert min_window("aa", "aa") == "aa"
        assert min_window("abc", "") == ""


class TestBinarySearch:
    def test_lower_bound(self):
        assert lower_bound([1, 2, 4, 4, 5], 4) == 2
        assert lower_bound([1, 2, 4, 4, 5], 3) == 2
        assert lower_bound([1, 2, 3], 10) == 3
        assert lower_bound([], 1) == 0

    def test_search_rotated(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        assert search_rotated(nums, 0) == 4
        assert search_rotated(nums, 3) == -1
        assert all(search_rotated(nums, v) == i for i, v in enumerate(nums))
        assert search_rotated([1], 1) == 0

    def test_min_ship_capacity(self):
        assert min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
        assert min_ship_capacity([3, 2, 2, 4, 1, 4], 3) == 6
        assert min_ship_capacity([1, 2, 3, 1, 1], 4) == 3


class TestIntervals:
    def test_merge_intervals(self):
        assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
        assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
        assert merge_intervals([[5, 6], [1, 10]]) == [[1, 10]]
        assert merge_intervals([]) == []

    def test_min_meeting_rooms(self):
        assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
        assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
        assert min_meeting_rooms([[1, 5], [5, 10]]) == 1
        assert min_meeting_rooms([]) == 0


class TestMonotonicStack:
    def test_daily_temperatures(self):
        assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
        assert daily_temperatures([30, 30]) == [0, 0]

    def test_largest_rectangle(self):
        assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
        assert largest_rectangle([2, 4]) == 4
        assert largest_rectangle([]) == 0


class TestHeaps:
    def test_top_k_frequent(self):
        assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
        assert top_k_frequent([4], 1) == [4]

    def test_kth_largest(self):
        assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
        assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    def test_merge_k_sorted(self):
        assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
        assert merge_k_sorted([[], [], [7]]) == [7]
        assert merge_k_sorted([]) == []


class TestGraphs:
    def test_num_islands(self):
        grid = ["11000", "11000", "00100", "00011"]
        assert num_islands(grid) == 3
        assert num_islands(["0"]) == 0
        assert num_islands([]) == 0

    def test_course_order(self):
        order = course_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        position = {course: i for i, course in enumerate(order)}
        assert len(order) == 4
        assert position[0] < position[1] < position[3]
        assert position[0] < position[2] < position[3]

    def test_course_order_cycle(self):
        assert course_order(2, [[1, 0], [0, 1]]) == []

    def test_shortest_path_grid(self):
        assert shortest_path_grid(["..#", "#..", "#.."]) == 4
        assert shortest_path_grid([".#", "#."]) == -1
        assert shortest_path_grid(["."]) == 0


class TestBacktracking:
    def test_subsets(self):
        result = subsets([1, 2, 3])
        assert len(result) == 8
        assert sorted(map(sorted, result)) == sorted(
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        )

    def test_permutations(self):
        result = permutations([1, 2, 3])
        assert len(result) == 6
        assert len({tuple(p) for p in result}) == 6

    def test_combination_sum(self):
        assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
        assert combination_sum([2], 1) == []


class TestDynamicProgramming:
    @pytest.mark.parametrize(("n", "ways"), [(0, 1), (1, 1), (2, 2), (3, 3), (5, 8), (10, 89)])
    def test_climb_stairs(self, n, ways):
        assert climb_stairs(n) == ways

    def test_coin_change(self):
        assert coin_change([1, 2, 5], 11) == 3
        assert coin_change([2], 3) == -1
        assert coin_change([1], 0) == 0
        assert coin_change([1, 3, 4], 6) == 2  # greedy would pick 4+1+1

    def test_house_robber(self):
        assert house_robber([1, 2, 3, 1]) == 4
        assert house_robber([2, 7, 9, 3, 1]) == 12
        assert house_robber([]) == 0

    def test_longest_common_subsequence(self):
        assert longest_common_subsequence("abcde", "ace") == 3
        assert longest_common_subsequence("abc", "def") == 0
        assert longest_common_subsequence("", "abc") == 0


class TestUnionFind:
    def test_count_components(self):
        assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
        assert count_components(3, []) == 3

    def test_redundant_connection(self):
        assert redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
        assert redundant_connection([[1, 2], [2, 3]]) is None


class TestTrie:
    def test_insert_search_prefix(self):
        trie = Trie()
        for word in ["apple", "app", "apply", "bat"]:
            trie.insert(word)
        assert trie.search("app") is True
        assert trie.search("ap") is False
        assert trie.starts_with("ap") is True
        assert trie.starts_with("c") is False
        assert trie.words_with_prefix("app") == ["app", "apple", "apply"]
        assert trie.words_with_prefix("z") == []


class TestLRUCache:
    def test_eviction_order(self):
        cache: LRUCache[int, str] = LRUCache(2)
        cache.put(1, "one")
        cache.put(2, "two")
        assert cache.get(1) == "one"  # 1 becomes most recent
        cache.put(3, "three")  # evicts 2
        assert cache.get(2) is None
        assert cache.get(3) == "three"
        assert len(cache) == 2

    def test_update_refreshes_recency(self):
        cache: LRUCache[str, int] = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)
        cache.put("c", 3)  # evicts b, not a
        assert cache.get("a") == 10
        assert cache.get("b") is None

    def test_rejects_bad_capacity(self):
        with pytest.raises(ValueError):
            LRUCache(0)
