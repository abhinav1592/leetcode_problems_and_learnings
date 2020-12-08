'''
1329. Sort the Matrix Diagonally
Link: https://leetcode.com/problems/sort-the-matrix-diagonally/

Time complexity: O(m*n*( log (min(m,n))))
Space complexity: O(m*n)

'''

class Solution:
    def diagonalSort(self, mat):
        d = dict()
        f = dict()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (i - j in d):
                    d[i - j].append(mat[i][j])
                else:
                    d[i - j] = [mat[i][j]]
        # print(d)
        for key in d:
            d[key].sort(reverse=1)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = d[i - j].pop()
        return mat

print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))