class Branch:
    class Node:
        def __init__(self, value: int, previous_element, next_element):
            self.value = value
            self.next = next_element
            self.prev = previous_element

        def __str__(self):
            return str(self.value)

    def __init__(self, number: int):
        self.head = self.Node(0, None, None)
        self.tail = self.Node(0, None, None)
        self.elements = 0
        self.tail.prev = self.head.prev = self.head
        self.head.next = self.tail.next = self.tail
        run = number
        while run > 1:
            self.add(run)
            if run % 2 is 0:
                run = run // 2
            else:
                run = 3*run + 1
        self.add(1)

    def __str__(self):
        walk = self.head
        out = []
        while not walk.next == walk.next.next:
            walk = walk.next
            out.append(walk.value)
        return str(out)

    def add(self, number: int):
        ntl = self.tail.prev
        new_node = self.Node(number, ntl, self.tail)
        self.tail.prev = ntl.next = new_node
        self.elements += 1

    def path_length(self):
        return self.elements

    def first_element(self):
        return self.head.next.value

    def __lt__(self, other):
        if self.path_length() < other.path_length():
            return True
        else:
            return False
