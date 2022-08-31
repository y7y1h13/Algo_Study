from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        N = 9
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        for r in range(N):
            for c in range(N):
                val = board[r][c]

                if val == '.':
                    continue

                if val in row[r]:
                    return False
                row[r].append(val)

                if val in col[c]:
                    return False
                col[c].append(val)

                idx = (r // 3) * 3 + c // 3
                if val in box[idx]:
                    return False
                box[idx].append(val)

        return True


ob1 = Solution()
print(ob1.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                         [".", "4", ".", "3", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                         [".", ".", "2", ".", "7", ".", ".", ".", "."],
                         [".", "1", "5", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", "2", ".", ".", "."],
                         [".", "2", ".", "9", ".", ".", ".", ".", "."],
                         [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
