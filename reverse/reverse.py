class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head == None:
            return None
        # set current node to current head
        current_node = self.head
        # prev == None, 1st go;
        prev = None

        while current_node is not None:
            # store current node's next
            next = current_node.next_node
            # current node's next becomes the prev
            current_node.next_node = prev
            # prev becomes current node 
            prev = current_node
            # current node become the value stored as next
            current_node = next
        # loop keeps running until it reaches end of list, 
        
        # original end of list becomes new head
        self.head = prev
