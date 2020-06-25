class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s = [str(i) for i in A]
        n = int(''.join(s)) + 1
        finallst = [int(i) for i in str(n)]
        return (finallst)
