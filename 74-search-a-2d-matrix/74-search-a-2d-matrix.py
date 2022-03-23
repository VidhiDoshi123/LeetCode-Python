class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bse_array(array,low,high,target):
            if(low<=high):
                mid =  (high + low) // 2
                if(array[mid] == target):
                    return True
                elif(target <array[mid]):
                    return bse_array(array,low,mid-1,target)
                elif(target > array[mid]):
                    return bse_array(array,mid+1,high,target)
            return False
        for i in range(0,len(matrix)):
            row = matrix[i]
            result =bse_array(row,0,len(row)-1,target)
            if(result):
                return True
        return False