class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trim_string = s.strip()
        split_str = trim_string.split(" ")
        return len(split_str[len(split_str) -1])
        