class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            temp_list = [[1],[1,1]]
            for i in range(3,numRows+1):
                print(i)
                last_row = temp_list[len(temp_list) -1]
                print(last_row)
                pascal_last_row = [0]*i
                for j in range(0,i):
                    print("hi" + str(j))
                    if j ==0 or j== i-1:
                        pascal_last_row[j] =1
                    else:
                        print("in else")
                        pascal_last_row[j] = last_row[j] + last_row[j-1]
                temp_list.append(pascal_last_row)
        return temp_list
                
        