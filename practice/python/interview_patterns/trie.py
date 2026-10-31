"""Pattern 12: tries for prefix queries."""

from __future__ import annotations


class Trie:
    def __init__(self) -> None:
        self.children: dict[str, Trie] = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())
        node.is_word = True

    def _walk(self, prefix: str) -> Trie | None:
        node: Trie | None = self
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def words_with_prefix(self, prefix: str) -> list[str]:
        """All stored words beginning with prefix, in sorted order."""
        found: list[str] = []

        def collect(node: Trie, acc: str) -> None:
            if node.is_word:
                found.append(acc)
            for ch in sorted(node.children):
                collect(node.children[ch], acc + ch)

        start = self._walk(prefix)
        if start is not None:
            collect(start, prefix)
        return found
