class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        
        key = defaultdict(int)
        for char in t:
            key[char] += 1

        letters = len(key)
        window = defaultdict(int)
        count = 0
        l = 0
        r = 0
        min_length = float('inf')
        res = ""

        while r < m:
            char_r = s[r]
            if char_r in key:
                window[char_r] += 1
                if window[char_r] == key[char_r]:
                    count += 1
            
            while count == letters:
                current_length = r - l + 1
                if current_length < min_length:
                    min_length = current_length
                    res = s[l : r + 1]
                
                char_l = s[l]
                if char_l in key:
                    window[char_l] -= 1
                    if window[char_l] < key[char_l]:
                        count -= 1
                l += 1
            r += 1

        return res