class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class QueueBusiness():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        if self.size == 0:
            node = Node(x)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node = Node(x)
            self.tail.next_item = node
            self.tail = node
            self.size += 1

    def get(self):
        if self.is_empty():
            return 'error'
        else:
            x = self.head.value
            self.head = self.head.next_item
            self.size -= 1
            return x


def main():
    num_command = int(input())
    queue_sized = QueueBusiness()
    list_stack = []
    for command in range(num_command):
        command = str(input())
        list_stack.append(command)
    for command in list_stack:
        if command == 'get':
            print(queue_sized.get())
        elif command == 'size':
            print(queue_sized.size)
        else:
            list_command = command.split()
            queue_sized.put(list_command[1])


if __name__ == '__main__':
    main()
