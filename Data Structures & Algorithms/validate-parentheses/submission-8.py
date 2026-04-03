class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_p=set(['{','[','('])
        for para in s:
            if para in open_p:
                stack.append(para)
            else:
                if len(stack) > 0:
                    check = stack.pop()
                    if check == "(" and para == ")":
                        pass
                    elif check == "{" and para == "}":
                        pass
                    elif check == "[" and para == "]":
                        pass
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0 