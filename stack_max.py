class StackMax:
    def __init__(self):
        self.items = []
        self.max = 0

    def push(self, item):
        if item > self.max:
            self.max = item
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if self.max == 0:
            print(None)
        else:
            print(self.max)


def read_input():
    n = int(input())
    items_stack = StackMax()
    list_stack = []
    for i in range(n):
        method = str(input())
        list_stack.append(method)
    for i in list_stack:
        if i == 'get_max':
            items_stack.get_max()
        elif i == 'pop':
            items_stack.pop()
        else:
            list_method = i.split()
            items_stack.push(int(list_method[1]))


def main():
    read_input()


if __name__ == "__main__":
    main()
