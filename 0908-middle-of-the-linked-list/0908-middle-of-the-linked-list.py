class Solution(object):
    def middleNode(self, head):
        #Count total number of nodes
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        #Find middle position
        mid_index = count // 2
        
        #Traverse again to reach the middle node using a for loop
        current = head
        for _ in range(mid_index):
            current = current.next
        
        return current
