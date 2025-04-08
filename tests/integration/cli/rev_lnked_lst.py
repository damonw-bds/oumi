class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_iterative(head):
    prev = None
    current = head
    
    while current:
        # Store the next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = next_temp
    
    return prev

def reverse_recursive(head):
    # Base case: if head is None or we've reached the last node
    if not head or not head.next:
        return head
    
    # Recursive case: reverse the rest of the list
    rest = reverse_recursive(head.next)
    
    # Set head node's next's next to head
    head.next.next = head
    head.next = None
    
    return rest

# Helper function to create a linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)
    
    print("Original linked list:")
    print_list(head)
    
    # Reverse using iterative method
    reversed_head = reverse_iterative(head)
    print("Reversed linked list (iterative):")
    print_list(reversed_head)
    
    # Create a new list to demonstrate recursive method
    head = create_linked_list(arr)
    reversed_head = reverse_recursive(head)
    print("Reversed linked list (recursive):")
    print_list(reversed_head)