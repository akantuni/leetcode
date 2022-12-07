class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = []

        for num in A:
            squares.append(num ** 2)

        return sorted(squares)
