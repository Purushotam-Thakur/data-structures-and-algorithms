class Solution:
    def toLowerCase(self, str):
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)


class Solution2:
    def toLowerCase(self, str):
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)


class Solution3:
    def toLowerCase(self, str):
        return str.lower()
