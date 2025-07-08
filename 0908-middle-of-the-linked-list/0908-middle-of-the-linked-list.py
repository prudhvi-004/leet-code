class Solution(object):
    def middleNode(self, head):
        # Step 1: Count total number of nodes
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        # Step 2: Find middle position
        mid_index = count // 2
        
        # Step 3: Traverse again to reach the middle node using a for loop
        current = head
        for _ in range(mid_index):
            current = current.next
        
        return current
