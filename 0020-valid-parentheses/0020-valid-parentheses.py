class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pairs.values():  # opening brackets
                stack.append(char)
            elif char in pairs:  # closing brackets
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (optional)
                return False
        return not stack
