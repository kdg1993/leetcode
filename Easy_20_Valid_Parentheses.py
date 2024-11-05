class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braket_map = {'(':')', '[':']', '{':'}'}

        for char in s:
            if char in braket_map:
                stack.append(char)
            elif len(stack) == 0 or braket_map[stack.pop()] != char:
                return False
            else:
                pass

        return True if len(stack) == 0 else False