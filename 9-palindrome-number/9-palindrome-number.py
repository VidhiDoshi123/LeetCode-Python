class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_num = str(x)
        arr = list(string_num)
        start = 0
        end =len(arr) -1
        while start <= end:
            arr[start], arr[end] = arr[end] , arr[start]
            start = start + 1
            end = end -1
        print(arr)
        string_num2 =''
        for i in range(len(arr)):
            string_num2 = string_num2 + str(arr[i])
        print(string_num,string_num2)
        if(string_num == string_num2):
            return True
        return False
        