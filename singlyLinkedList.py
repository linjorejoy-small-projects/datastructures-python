class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return "Data: " + self.data 

class LinkedList:
    def __init__(self):
        self.head = None

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
        del temporaryNode

    def insert(self,newNode):
        self.insertEnd(newNode)
    
    def insertAt(self, newNode, position):
        if position < 0 or position >= self.listLength():
            print("Invalid Position. Out of Bounds")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        if position is self.listLength():
            self.insertEnd(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
    
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
            return
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def deleteHead(self):
        """Deletes the head of the LinkedList
        """
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
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
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode =currentNode.next
                currentPosition +=1
        else:
            print("List is Empty")

    def printList(self):
        """For printing the whole List
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
                    if currentNode.next is not None:
                        if(currentNode == NodeTwo):
                            secondNode = currentNode
                            secondNodePosition = position
                            break
                        previousOfSecondNode = currentNode
                        currentNode = currentNode.next
                        position += 1
                    else:
                        break
                break
            elif(currentNode == NodeTwo):
                previousOfSecondNode = previousNode
                secondNode = NodeTwo
                secondNodePosition = position
                previousOfFirstNode = currentNode
                currentNode = currentNode.next
                position += 1
                while True:
                    if currentNode.next is not None:
                        if(currentNode == NodeOne):
                            firstNode = currentNode
                            firstNodePosition = position
                        previousOfFirstNode = currentNode
                        currentNode = currentNode.next
                        position += 1
                    else:
                        break
                break
            previousNode = currentNode
            currentNode = currentNode.next
            position += 1

        # Swapping
        if(firstNodePosition == 0):
            tempNode = secondNode.next
            secondNode.next = firstNode.next
            firstNode.next = tempNode
            previousOfSecondNode.next = firstNode
            self.head = secondNode
        elif(secondNodePosition == 0):
            tempNode = firstNode.next
            print(tempNode)
            firstNode.next = secondNode.next
            print(firstNode)
            secondNode.next = tempNode
            print(secondNode)
            previousOfFirstNode.next = secondNode
            print(previousOfFirstNode)
            self.head = firstNode
            print(self.head)
        else:
            tempNode = secondNode.next
            secondNode.next = firstNode.next
            previousOfFirstNode.next = secondNode
            previousOfSecondNode.next = firstNode
            firstNode.next = tempNode

    def swapbyData(self, NodeOneData, NodeTwoData):
        """Used to swap the position of the two nodes in the linkedList by the data

        Args:
            NodeOneData (String): First Node Data
            NodeTwoData (String): Second Node Data
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
            tempNode = secondNode.next
            secondNode.next = firstNode.next
            firstNode.next = tempNode
            previousOfSecondNode.next = firstNode
            self.head = secondNode
        elif(secondNodePosition == 0):
            tempNode = firstNode.next
            firstNode.next = secondNode.next
            firstNode.next = tempNode
            previousOfFirstNode.next = secondNode
            self.head = firstNode
        else:
            tempNode = secondNode.next
            secondNode.next = firstNode.next
            previousOfFirstNode.next = secondNode
            previousOfSecondNode.next = firstNode
            firstNode.next = tempNode

    def bubbleSort(self):
        while True:
            swaps = 0
            currNode = self.head
            while True:
                if(currNode.next != None):
                    if(currNode.data > currNode.next.data):
                        previousNode = currNode.next
                        self.swapbyNodes(currNode,currNode.next)
                        currNode = previousNode
                        swaps += 1
                    currNode = currNode.next
                else:
                    break
            if(swaps == 0):
                break

    def sort(self):
        pass





one = Node("Ava")
two = Node("Adam")
three = Node("Ben10")
four = Node("Darth Vader")

linkedList = LinkedList()
linkedList.insert(one)
linkedList.insert(two)
linkedList.insert(three)
linkedList.insert(four)

linkedList.printList()
print("*"*10)
linkedList.swapbyNodes(two,one)
linkedList.printList()
print("*"*10)
linkedList.bubbleSort()
linkedList.printList()