class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 | len(s) == 1:
            return True
        ss = re.sub(r'[^a-zA-Z0-9]', '', s)
        ss = ss.lower()
        print(ss)
        l, r = 0, len(ss)-1
        while l < r:
            # print(ss[r], ss[l])
            if ss[l] == ss[r]:
                l += 1
                r -= 1
            else:
                return False
        return True