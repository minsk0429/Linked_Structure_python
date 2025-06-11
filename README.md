# Linked_Structure_python

Data structure implemented in Python (linked structures)

---

# Linked Structures in Data Structures

## 📋 Linked Structures

**Linked structures** are a family of dynamic data structures where elements (nodes) are linked together via references (or pointers). Each node typically contains data and one or more references to other nodes. Unlike arrays or Python lists, linked structures do not require contiguous memory allocation, allowing flexible and efficient insertion and deletion.

Common linked structures include:
- **Linked List**: nodes linked sequentially (singly, doubly, or circularly)  
- **Linked Stack**: stack implemented using linked nodes  
- **Circularly Linked Queue**: queue with a circular linked list to efficiently manage front and rear  
- And many more variants built on linked nodes  

---

## Characteristics
- Nodes contain data and references (pointers) to other nodes  
- Memory allocation is dynamic, not contiguous  
- Enables efficient insertion and deletion without shifting elements  
- No direct indexing (no random access) — traversal needed  
- Variants differ by number and direction of links:
  - **Singly linked**: each node points to next node only  
  - **Doubly linked**: nodes point to both next and previous  
  - **Circularly linked**: last node points back to first, forming a loop  

---

## Example (Python - Singly Linked List Node & Append)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage example
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()  # Output: 10 -> 20 -> 30 -> None
```

---

## Use Cases

- Implementing dynamic data collections that grow/shrink efficiently
- Building stacks, queues, and other abstract data types without fixed size limits
- Undo-redo systems where operations are tracked in linked nodes
- Navigating back and forth in applications (e.g., browser history, playlists)
- Circular buffers or queues requiring wrap-around behavior

___

## 🚀 Summary

| Feature              | Linked List         | Linked Stack        | Circularly Linked Queue |
|----------------------|---------------------|---------------------|------------------------|
| Structure            | Nodes linked linearly (singly/doubly) | Stack implemented with linked nodes (LIFO) | Queue using circular linked nodes (FIFO) |
| Insertion            | Anywhere (with reference) | Top only            | Rear only              |
| Deletion             | Anywhere (with reference) | Top only            | Front only             |
| Ordering             | Linear              | LIFO                | FIFO                   |
| Memory Allocation    | Dynamic, non-contiguous | Dynamic, non-contiguous | Dynamic, non-contiguous  |
| Indexable            | No                  | No                  | No                     |
| Use Cases            | Dynamic lists, navigation, undo systems | Undo/redo, function calls | Task scheduling, buffering |

___
The attached codes are linked structures implemented in Python including Linked stack class, linked list class, circularly linked queue class, and deck implemented with doubly linked structure.
