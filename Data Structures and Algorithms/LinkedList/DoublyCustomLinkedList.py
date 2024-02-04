# Creating custom linked list
class DoublyNode:
    
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return self.data
    
class DoublyLinkedList:
    
    def __init__(self,circular):
        self.head = None
        self.circular = circular
        
        
    def  __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
            
        if(self.circular):
            nodes.insert(0,str(nodes[-1]))
            nodes.append(str(self.head))
        else:
            nodes.append("None")
            nodes.insert(0,"None")
        return " <-> ".join(nodes)

# Using Custom Single LinkedList
llist = DoublyLinkedList(circular=True)

# Nodes
first_node = DoublyNode("a")
second_node = DoublyNode("b")
third_node = DoublyNode("c")

llist.head = first_node
first_node.next = second_node
second_node.next = third_node

# LinkedList
if(llist.circular):
    print("Doubly Circular Linked List")
    print(llist)
else:
    print("Doubly Linked List")
    print(llist)