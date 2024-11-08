# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flat(nested):
            rslt = []
            
            for element in nested:

                if element.isInteger():
                    rslt.append(element.getInteger())
                else:
                    rslt.extend(flat(element.getList()))

            return rslt

        self.flattened = deque(flat(nestedList))


    def next(self) -> int:
        out = self.flattened.popleft()
        
        return out
    
    def hasNext(self) -> bool:
        if len(self.flattened) > 0:
            return True
        else:
            return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())