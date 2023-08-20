class Solution:
    def init(self):
        pass

    def find_missing_in_array(self, list_of_elements):
        self.list_of_elements = list_of_elements
        x = []
        for i in range(1, len(self.list_of_elements)+1):
            if i not in self.list_of_elements:
                x.append(i)

        return x


l = Solution()
print(l.find_missing_in_array([4, 3, 2, 7, 8, 2, 3, 1]))