class node():                   # basic singly linked list implementation
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list( node ):
    def __init__(self, node):
        self.head = node

    def remove_dups(self): # solution to first part of the problem
        seen_vals = {self.head.data}
        node = self.head
        while node.next != None:
            val = node.next.data
            if val in seen_vals:
                node.next = node.next.next
            else:
                node = node.next

    def remove_dups_no_buffer(self): # solution to the second part of the problem
        node = self.head
        while node != None:
            self.runner_remove_forward(node)
            node = node.next


    def runner_remove_forward(self, node): # uses a 'runner' to remove all values that match the current value
        seen_val = node.data
        while node.next != None:
            curr_val = node.next.data
            if curr_val == seen_val:
                node.next = node.next.next
            else:
                node = node.next

    def print_list(self): # utility print method to check implementation
        node = self.head
        print(node.data)
        while node.next != None:
            print(node.next.data)
            node = node.next

############ TESTING ##############
n1 = node(1)
n2 = node(2)
n3 = node(1)
n4 = node(3)
n5 = node(1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

the_list = linked_list(n1) #create two lists
second_list = the_list
the_list.remove_dups()
the_list.print_list() # expected 1,2,3
second_list.remove_dups_no_buffer()
second_list.print_list() # expected 1,2,3
