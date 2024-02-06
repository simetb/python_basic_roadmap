class QuequeNode:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queque:
    def __init__(self, data):
        self.head = QuequeNode(data)
        self.count = 1  # Aquí se corrigió el valor inicial del contador

    def __str__(self):
        queque_str = ""
        node = self.head
        while node:
            queque_str += str(node.value) + "->"
            node = node.next
        return queque_str[:-2]

    def push(self, value):
        new_node = QuequeNode(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
        self.count += 1
        
    def quequeSize(self):
        return self.count
    
    def pop(self):
        if(self.quequeSize() == 0):
            Exception("You cant pop a queque with a zero length ")
        remove = self.head.value
        self.head = self.head.next
        self.count -=1
        return remove

if __name__ == "__main__":
    queque = Queque(1)
    queque.push(2)
    queque.push(3)
    
    print(queque)
    remove = queque.pop()
    
    print("Removing fon queque: ")
    print(remove)
    
    print("Queqe")
    print(queque)
