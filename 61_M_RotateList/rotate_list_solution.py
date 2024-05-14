
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLL(head: ListNode):
    for i in range(5):
        print(str(head.val) + '->')
        head = head.next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        for _ in range(k):
            prev = None
            current = head
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            current.next = head
            head = current
        print(printLL(head))
            


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2000000000
    solution = Solution()
    
    print(solution.rotateRight(head, k))