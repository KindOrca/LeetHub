class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = defaultdict(int)
        words = s.split(' ')
        if len(words) != len(pattern): return False
        for pat, word in zip(pattern, words):
            if dic[pat] == word: continue
            if dic[pat] and dic[pat] != word: return False
            if word in dic.values(): return False
            dic[pat] = word
        return True