#Create a class called Stack and implement the methods to push, pop and head using a list for storing the elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty , cannot pop")
    
    def head(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. No head element.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
my_stack = Stack()

# Push elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Print the current stack
print("Current Stack:", my_stack.items)

# Get and print the head element
print("Head element:", my_stack.head())

# Pop an element from the stack
popped_element = my_stack.pop()
print("Popped element:", popped_element)

# Print the updated stack
print("Updated Stack:", my_stack.items)
    