

# https://stackabuse.com/python-linked-lists/

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

nodes = []
nodes.append(ListNode(15))
nodes.append(ListNode(8.2))
nodes.append(ListNode(3))

track = SingleLinkedList()
for current_node in nodes:
    track.add_list_item(current_node)

track.print_all_nodes()

