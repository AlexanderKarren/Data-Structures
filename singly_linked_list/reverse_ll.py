from singly_linked_list import LinkedList

my_ll = LinkedList()
my_ll.add_to_tail(1)
my_ll.add_to_tail(2)
my_ll.add_to_tail(3)

print(my_ll.head.value, my_ll.head.next.value, my_ll.tail.value)


def reverse_ll(ll):
    # if LL is empty or only has one node
    if ll.head is None or ll.head is ll.tail:
        return ll
    else:
        current = ll.head
        prev = None
        next = None
        while current is not None:
            # store a pointer to the current next value
            next = current.next

            # switch current's next pointer to the previous
            current.next = prev

            # increment logic
            prev = current
            current = next

        ll.head, ll.tail = ll.tail, ll.head


reverse_ll(my_ll)
print(my_ll.head.value, my_ll.head.next.value, my_ll.tail.value)
