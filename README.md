# LinkedList Data Structures in python

Currently only the SinglyLinkedList, DoublyLinkedList has been added
* SinglyLinkedList  
* DoublyLinkedList

***

## SinglyLinkedList

    isListEmpty()
    listLength()
    getNodePosition()
    insertHead()
    insert()
    insertAt()
    insertEnd()
    deleteHead()
    deleteAt()
    printList()
    bubbleSort()

> Swap method not working


`swapByNodes()` and the `swapByData()` functions **NotWorking**

### LinkedList Class
```python
def __init__(self):
    self.head = None
```

### Node Class
```python
def __init__(self,data):
    self.data = data
    self.next = None

```

***
## DoublyLinkedList
>DoublyLinkedList is not complete

> Swap method not working


    isListEmpty()
    listLength()
    getNodePosition()
    insertHead()
    insert()
    insertAt()
    insertEnd()
    deleteHead()
    deleteAt()
    deleteTail()
    printList()
    printFromBeginning()
    printFromBack()
    bubbleSort()
> Swap method not working


`swapByNodes()` and the `swapByData()` functions **NotWorking**

### LinkedList Class
```python
def __init__(self):
    self.head = None
    self.tail = None
```
### Node Class
```python
def __init__(self,data):
    self.data = data
    self.next = None

```
***
Most of these functions are from a Udemy Course [Linked List Data Structures In Python](https://cognizantee.udemy.com/course/python-linked-list/learn/lecture/8122100#announcements "Udemy Course").

***