from Node import Node




 


class Stack:
    
    def __init__(self):
        self.top = None

    def __init__(self,data=None):
        self.top = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __str__(self):
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result[::-1]) if result else "A pilha está vazia"
