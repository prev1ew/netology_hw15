class Stack:
    def __init__(self):
        self.items = list()

    def isEmpty(self):
        return not self.items

    def push(self, new_element):
        self.items.insert(0, new_element)

    def peek(self):
        return self.items[0] if self.items else None

    def size(self):
        return len(self.items)

    def pop(self):
        try:
            return self.items.pop(0)
        except IndexError:
            return None

    def is_balanced(self, brackets="〈〉()[]{}"):
        opening, closing = brackets[::2], brackets[1::2]
        stack = []  # keep track of opening brackets types
        for character in self.items:
            if character in opening:  # bracket
                stack.append(opening.index(character))
            elif character in closing:  # bracket
                if stack and stack[-1] == closing.index(character):
                    stack.pop()
                else:
                    return False
        return not stack


test = Stack()
test.push(')')
test.push('(')
test.push('}')
test.push('{')
test.push(')')
test.push(')')
test.push('(')
test.push('(')
print(test.is_balanced())

