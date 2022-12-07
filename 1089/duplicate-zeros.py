class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        len_arr = len(arr)
        index_ls = []
        ind = -1
        
        for i in arr:
            ind += 1
            if i == 0:
                index_ls.append(ind)

        for i in index_ls:
            arr.insert(i + index_ls.index(i), 0)

        while len(arr) > len_arr:
            arr.pop(-1)
