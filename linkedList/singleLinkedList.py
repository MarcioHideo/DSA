class Node:
    def __init__(self, data):
        self.data = data # restore the data for the current Node
        self.next = None # for the next node you want to point

    def __str__(self):
        return (f"Data: {self.data}") 
    
    
class SingleLinkedList:
    def __init__(self):
        self.head = None

    # insert at head of linked list
    def insert_head(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def print_list(self):
        current_node = self.head
        while current_node is not None :
            print(f"{current_node.data}", end = " -> " if current_node.next is not None else "\n")
            current_node = current_node.next

    def insert_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return None

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
    
    def insert_index(self, data, index):
        ## check if the index is on the head
        if index == 0:
            self.insert_head(data)
            return None

        next_index = 1
        temp_node = self.head
        # Traverse the node
        while next_index != index and temp_node.next:
            temp_node = temp_node.next
            next_index+= 1

        if temp_node.next is None:
            raise IndexError("Index out of bounds")

        new_node = Node(data)
        new_node.next = temp_node.next
        temp_node.next = new_node


    def delete_head(self):
        # Removes the first node from the list
        if not self.head:
            print("No head to delete")
            return
        self.head = self.head.next

    def delete_tail(self):
        # Removes the last node from the list
        if not self.head:
            print("Zero nodes")
        
        if not self.head.next:
            self.head = None
        
        temp = self.head
        while not temp.next:
            temp = temp.next
        temp.next = None


    def delete_index(self, index):
        # Removes a node at a specific index
        if not self.head:
            print("no nodes")
            return None

        if index == 0:
            self.head = self.head.next
            return None

        next_index = 1
        temp_node = self.head
        # Traverse the node
        while next_index != index and temp_node.next:
            temp_node = temp_node.next
            next_index+= 1

        if temp_node.next is None:
            raise IndexError("Index out of bounds")

        temp_node.next = temp_node.next.next



    def delete_value(self, value):
        # Removes the first node that matches the value
        if not self.head:
            print("No nodes")
            return None
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next and temp.next.data != value: 
            temp = temp.next
        
        if not temp.next:
            raise IndexError("Out of bounds")
        
        temp.next = temp.next.next
        


    def contains(self, value):
        # Returns True if value is found in the list
        if not self.head:
            print("No nodes")
            return None
        
       
        temp = self.head
        while temp.next and temp.data != value: 
            temp = temp.next
        
        
        
        return (temp.data == value)

    def length(self):
        # Returns the number of nodes in the list
        count = 1
        current = self.head
        if not self.head:
            return 0

        while current.next:
            current = current.next
            count+=1

        return count


    def to_list(self):
        # Converts the linked list to a Python list
        current = self.head
        new_list = []
        while current:
            new_list.append(current.data)
            current = current.next

        return new_list

    def reverse(self):
        # Reverses the linked list in place
        # Converts the linked list to a Python list
        current = self.head

        # create a list from the current one
        all_values = self.to_list()
        self.head = None
        for i in reversed(all_values):
            self.insert_tail(i)
        
        return None

    def get_middle(self):
        # Returns the middle node of the list
        length = self.length()
        if not self.head:
            return None
        
        print(length)

        middle_index = round(length / 2)
        current = self.head
        while middle_index > 0:
            current = current.next
            middle_index-=1
        
        return current
        


    def has_cycle(self):
        # Detects if the list has a loop (cycle)
        if not self.head:
            return None

        current = self.head.next
        while current and current != self.head:
            current = current.next

        # it returns cycle if one of the nodes is equal to head
        if current == self.head:
            return True
    
        return False

    
    




if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    print(ll.contains(2))


