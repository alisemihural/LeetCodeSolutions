# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentl1 = l1
        currentl2 = l2
        currentl3 = ListNode()
        headl3 = currentl3

        while (currentl1 != None or currentl2 != None):
            
            #L3 node calculation
            if (currentl2 == None):
                currentl3.val += currentl1.val
            elif (currentl1 == None):
                currentl3.val += currentl2.val
            else:
                currentl3.val = currentl1.val + currentl2.val + currentl3.val

            #Carry
            newVal = 0
            if(currentl3.val > 9):
                currentl3.val = currentl3.val - 10
                newVal = 1
            
            #Create the next node of L3
            if (currentl2 != None):
                if(currentl2.next != None):
                    newNode = ListNode(newVal)
                    currentl3.next = newNode
                if(newVal == 1):
                    newNode = ListNode(newVal)
                    currentl3.next = newNode
            if (currentl1 != None):
                if(currentl1.next != None):
                    newNode = ListNode(newVal)
                    currentl3.next = newNode
                if(newVal == 1):
                    newNode = ListNode(newVal)
                    currentl3.next = newNode
            
            #Next column
            if (currentl1 != None):
                currentl1 = currentl1.next
            if (currentl2 != None):
                currentl2 = currentl2.next
            currentl3 = currentl3.next
        
        return headl3
        

