class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_num= ""
        for i in digits:
            string_num = string_num + str(i)
        num = int(string_num)
        ans = str(num + 1)
        ans_arr = list(ans)
        return ans_arr
        
        