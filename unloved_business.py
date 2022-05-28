# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    # Your code
    # ヽ(´▽`)/
    head = node
    if idx == 0:
        return head.next_item
    elif idx == 1:
        del_node = head.next_item
        head.next_item = del_node.next_item
        return head
    else:
        index = idx - 1
        while index:
            node = node.next_item
            index -= 1
        del_node = node.next_item
        node.next_item = del_node.next_item
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0, 1)
    # result is node0 -> node2 -> node3
