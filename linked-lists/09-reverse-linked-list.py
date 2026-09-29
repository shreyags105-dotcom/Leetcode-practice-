class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def build_linked_list(values):
    head = None
    tail = None

    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def to_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values


if __name__ == "__main__":
    linked = build_linked_list([1, 2, 3, 4, 5])
    reversed_linked = reverse_list(linked)
    assert to_list(reversed_linked) == [5, 4, 3, 2, 1]

    single = build_linked_list([7])
    assert to_list(reverse_list(single)) == [7]

    empty = None
    assert reverse_list(empty) is None
    print("Reverse Linked List tests passed.")
