class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
    
    def __str__(self):
        return "Data: " + self.data 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isListEmpty(self):
        if self.head is None:
            return True
        return False

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def getNodePosition(self, keyNode):
        count = 0
        currentNode = self.head
        while True:
            if(currentNode == keyNode):
                return count
            count += 1
            currentNode = currentNode.next
        return -1

    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        temporaryNode.previous = newNode
        del temporaryNode

    def insert(self,newNode):
        self.insertEnd(newNode)
    
    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid Position. Out of Bounds")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        if position is self.listLength():
            self.insertEnd(newNode)
            return     
        if(position <= self.listLength()//2):
            currentNode = self.head   
            currentPosition = 0
            while True:
                if currentPosition == position:
                    currentNode.previous.next = newNode
                    newNode.previous = currentNode.previous
                    newNode.next = currentNode
                    currentNode.previous = newNode
                    break
                currentNode = currentNode.next
                currentPosition += 1
        else:
            currentNode = self.tail
            currentPosition = self.listLength()-1
            while True:                
                if currentPosition == position:
                    currentNode.previous.next = newNode
                    newNode.previous = currentNode.previous
                    newNode.next = currentNode
                    currentNode.previous = newNode
                    break
                currentNode = currentNode.previous
                currentPosition -= 1
    
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.previous = lastNode
        self.tail = newNode
    
    def deleteHead(self):
        """Deletes the head of the LinkedList
        """
        if self.isListEmpty() is False:
            self.head = self.head.next
            self.head.previous.next = None
            self.head.previous = None
        else:
            print("Linked List is Empty")

    def deleteAt(self,position):
        """Delete a node at a specified position

        Args:
            position (Integer): The index value of the node to be deleted
        """
        if position < 0 or position >= self.listLength():
            print("Invalid Position. Out of Bounds")
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            if position is self.listLength():
                self.deleteTail()
                return
            if(position <= self.listLength()//20):
                currentNode = self.head
                currentPosition = 0
                while True:
                    if currentPosition == position:
                        currentNode.previous.next = currentNode.next
                        currentNode.next.previous = currentNode.previous
                        del currentNode
                        break
                    currentNode =currentNode.next
                    currentPosition +=1
            else:
                currentNode = self.tail
                currentPosition = self.listLength()-1
                while True:
                    if currentPosition == position:
                        currentNode.previous.next = currentNode.next
                        currentNode.next.previous = currentNode.previous
                        del currentNode
                        break
                    currentNode = currentNode.previous
                    currentPosition -= 1
        else:
            print("List is Empty")

    def deleteTail(self):
        self.tail.previous.next = None

    def printList(self):
        """For printing the whole List from the Beginning
        """
        if self.head is None:
            print("List is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode)
            currentNode = currentNode.next

    def printFromBeginning(self):
        """Similar to printList Function
        """
        self.printList()

    def printFromBack(self):
        """Print the Linked List in reverse order
        """
        if(self.tail is None):
            print("List is Empty")
            return
        currentNode = self.tail
        while True:
            if currentNode is None:
                break
            print(currentNode)
            currentNode = currentNode.previous
    
    def swapbyNodes(self, NodeOne, NodeTwo):
        """Used to swap the position of the two nodes in the linkedList

        Args:
            NodeOne (Node): First Node
            NodeTwo (Node): Second Node
        """
        currentNode = self.head
        previousNode = None
        position = 0
        while True:
            # Finding Position of Node
            if(currentNode == NodeOne):
                previousOfFirstNode = previousNode
                firstNode = currentNode                
                firstNodePosition = position
                currentNode = currentNode.next
                previousOfSecondNode = currentNode
                while True:
                    if(currentNode == NodeTwo):
                        secondNode = currentNode
                        secondNodePosition = position
                        break
                    previousOfSecondNode = currentNode
                    currentNode = currentNode.next
                    position += 1
                break
            elif(currentNode == NodeTwo):
                previousOfSecondNode = previousNode
                secondNode = NodeTwo
                secondNodePosition = position
                currentNode = currentNode.next
                previousOfFirstNode = currentNode
                while True:
                    if(currentNode == NodeOne):
                        firstNode = currentNode
                        secondNodePosition = position
                    previousOfFirstNode = currentNode
                    currentNode = currentNode.next
                    position += 1
            previousNode = currentNode
            currentNode = currentNode.next
            position += 1

        # Swapping
        if(firstNodePosition == 0):
            tempPrevNode = secondNode.previous
            tempPostNode = secondNode.next
            secondNode.previous = None
            secondNode.next = firstNode.next
            firstNode.next = tempPostNode
            tempPrevNode.next = firstNode
            self.head = secondNode
            del tempPostNode
            del tempPrevNode
        elif(secondNodePosition == 0):
            tempPrevNode = firstNode.previous
            tempPostNode = firstNode.next
            firstNode.previous = None
            firstNode.next = secondNode.next
            secondNode.next = tempPostNode
            secondNode.previous = tempPrevNode
            self.head = firstNode
            del tempPostNode
            del tempPrevNode
        else:
            tempPrevNode = secondNode.previous
            tempPostNode = secondNode.next
            secondNode.next = firstNode.next
            secondNode.previous = firstNode.previous
            firstNode.next = tempPostNode
            firstNode.previous = tempPrevNode
            del tempPostNode
            del tempPrevNode

    def swapbyData(self, NodeOneData, NodeTwoData):
        """Used to swap the position of the two nodes in the linkedList

        Args:
            NodeOneData (Node): First Node
            NodeTwoData (Node): Second Node
        """
        currentNode = self.head
        previousNode = None
        position = 0
        while True:
            # Finding Position of Node
            if(currentNode.data == NodeOneData):
                previousOfFirstNode = previousNode
                firstNode = currentNode                
                firstNodePosition = position
                currentNode = currentNode.next
                previousOfSecondNode = currentNode
                while True:
                    if(currentNode.data == NodeTwoData):
                        secondNode = currentNode
                        secondNodePosition = position
                        break
                    previousOfSecondNode = currentNode
                    currentNode = currentNode.next
                    position += 1
                break
            elif(currentNode.data == NodeTwoData):
                previousOfSecondNode = previousNode
                secondNode = NodeTwoData
                secondNodePosition = position
                currentNode = currentNode.next
                previousOfFirstNode = currentNode
                while True:
                    if(currentNode.data == NodeOneData):
                        firstNode = currentNode
                        secondNodePosition = position
                    previousOfFirstNode = currentNode
                    currentNode = currentNode.next
                    position += 1
            previousNode = currentNode
            currentNode = currentNode.next
            position += 1

        # Swapping
        if(firstNodePosition == 0):
            tempPrevNode = secondNode.previous
            tempPostNode = secondNode.next
            secondNode.previous = None
            secondNode.next = firstNode.next
            firstNode.next = tempPostNode
            tempPrevNode.next = firstNode
            self.head = secondNode
            del tempPostNode
            del tempPrevNode
        elif(secondNodePosition == 0):
            tempPrevNode = firstNode.previous
            tempPostNode = firstNode.next
            firstNode.previous = None
            firstNode.next = secondNode.next
            secondNode.next = tempPostNode
            secondNode.previous = tempPrevNode
            self.head = firstNode
            del tempPostNode
            del tempPrevNode
        else:
            tempPrevNode = secondNode.previous
            tempPostNode = secondNode.next
            secondNode.next = firstNode.next
            secondNode.previous = firstNode.previous
            firstNode.next = tempPostNode
            firstNode.previous = tempPrevNode
            del tempPostNode
            del tempPrevNode

    # def bubbleSort(self):
    #     while True:
    #         swaps = 0
    #         currNode = self.head
    #         while True:
    #             if(currNode.next != None):
    #                 if(currNode.data > currNode.next.data):
    #                     previousNode = currNode.next
    #                     self.swapbyNodes(currNode,currNode.next)
    #                     currNode = previousNode
    #                     swaps += 1
    #                 currNode = currNode.next
    #             else:
    #                 break
    #         if(swaps == 0):
    #             break
            
    # def sort(self):
    #     pass





one = Node("Darth Vader")
two = Node("Adam")
three = Node("Ben10")
four = Node("Ava")
one1 = Node("Darth Vader")
two2 = Node("Adam")
three3 = Node("Ben10")
four4 = Node("Ava2")

linkedList = LinkedList()
linkedList.insert(one)
linkedList.insert(two)
linkedList.insert(three)
linkedList.insert(one1)
linkedList.insert(two2)
linkedList.insert(three3)


print(linkedList.listLength())

linkedList.insertAt(four,5)
print("#"*10)
linkedList.insertAt(four4,5)
linkedList.printList()
linkedList.deleteAt(5)
print("*"*10)
linkedList.printList()

print("*%"*10)
linkedList.swapbyData("Ava","Adam")
linkedList.printList()