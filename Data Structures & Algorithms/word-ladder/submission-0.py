from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        q = deque([beginWord])
        visit = set([beginWord])
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + ch + word[i + 1:]
                        if nxt in words and nxt not in visit:
                            visit.add(nxt)
                            q.append(nxt)
            steps += 1

        return 0