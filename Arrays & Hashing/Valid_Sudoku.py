class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cross3 = {}
        for i in range(3):
            for j in range(3):
                cross3 = {}
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        if board[x][y] != '.':
                            if board[x][y] not in cross3:
                                cross3[board[x][y]] = ''
                            else:
                                return False
        
        
        Big_Location = {"1x":{}, "2x":{}, "3x":{}, "4x":{}, "5x":{}, "6x":{}, "7x":{}, "8x":{}, "9x":{}, "1y":{}, "2y":{}, "3y":{}, "4y":{}, "5y":{}, "6y":{}, "7y":{}, "8y":{}, "9y":{}}

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] != '.':
                    if x in Big_Location[board[x][y]+"x"] or y in Big_Location[board[x][y]+"y"]:
                        return False
                    else:
                        Big_Location[board[x][y]+"x"][x] = "f"
                        Big_Location[board[x][y]+"y"][y] = "f"
        
        return True
    
#My Solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(3):
            for j in range(3):
                dic = {}
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        if board[x][y] != '.':
                            if board[x][y] not in dic:
                                dic[board[x][y]] = 1
                            else:
                                return False

        
        y_location_dic = {i: [] for i in range(10)}
        x_location_dic = {i: [] for i in range(10)}


        for row in range( len(board) ):
            for cell in range( len(board[row]) ):
                if board[row][cell] != ".":

                    if board[row][cell] not in x_location_dic[row]:
                        if x_location_dic[row] is None:
                            x_location_dic[row] = board[row][cell]
                        x_location_dic[row].append( board[row][cell] )
                    else:
                        return False

                    if board[row][cell] not in y_location_dic[cell]:
                        if y_location_dic[cell] is None:
                            y_location_dic[cell] = board[row][cell]
                        y_location_dic[cell].append( board[row][cell] )
                    else:
                        return False

        return True

                        