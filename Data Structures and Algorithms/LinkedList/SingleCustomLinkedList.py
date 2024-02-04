# Creating custom linked list
class SingleNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return self.data
    
class SingleLinkedList:
    def __init__(self,circular):
        self.head = None
        self.circular = circular
            
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None") if not self.circular else nodes.append(str(self.head))
        return " -> ".join(nodes)

# Using Custom Single LinkedList
llist = SingleLinkedList(circular=True)

# Nodes
first_node = SingleNode("a")
second_node = SingleNode("b")
third_node = SingleNode("c")

llist.head = first_node
first_node.next = second_node
second_node.next = third_node

# LinkedList
if(llist.circular):
    print("Single Circular Linked List")
    print(llist)
else:
    print("Single Linked List")
    print(llist)

