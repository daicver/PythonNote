class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h_num = len(matrix)
        v_num = len(matrix[0])

        L, R, T, B = 0, v_num, 0, h_num
        out = []
        while True:
            for i in range(L, R): out.append(matrix[T][i])
            T += 1
            if T >= B: break
            
            for i in range(T, B): out.append(matrix[i][R-1])
            R -= 1
            if L >= R: break

            for i in range(R-1, L-1, -1): out.append(matrix[B-1][i])
            B -= 1
            if T >= B: break

            for i in range(B-1, T-1, -1): out.append(matrix[i][L])
            L += 1
            if L >= R: break

        return out
